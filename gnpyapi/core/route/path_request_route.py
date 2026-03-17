# coding: utf-8
import json
from pathlib import Path
from typing import Any

from fastapi import Body

from gnpyapi.core import app
from gnpyapi.core.exception.equipment_error import EquipmentError
from gnpyapi.core.exception.topology_error import TopologyError
from gnpyapi.core.service.path_request_service import PathRequestService
from gnpy.tools.convert_legacy_yang import yang_to_legacy
from gnpyapi.core import API_VERSION

PATH_REQUEST_BASE_PATH = '/path-request'
_EXAMPLE = json.loads(
    (Path(__file__).parents[2] / 'exampledata' / 'planning_demand_example.json').read_text()
)
_EXAMPLES = {'planning-demand': {'summary': 'Planning demand request', 'value': _EXAMPLE}}
_SCHEMA = {'type': 'object', 'example': _EXAMPLE}


@app.post(API_VERSION + PATH_REQUEST_BASE_PATH, status_code=201)
def path_request(
    data: Any = Body(..., openapi_examples=_EXAMPLES, json_schema_extra=_SCHEMA)
):
    is_legacy = 'gnpy-api:api' not in data
    if not is_legacy:
        api_data = json.loads(data) if isinstance(data, str) else data
        legacy_data = yang_to_legacy(api_data)
        service = legacy_data['gnpy-path-computation:services']
        topology = legacy_data['gnpy-network-topology:topology']
        # TODO: yang_to_legacy is repeated due GNPy's bug
        equipment = yang_to_legacy(api_data["gnpy-api:api"]['gnpy-eqpt-config:equipment'])
    else:
        service = data['gnpy-api:service']
        if 'gnpy-api:topology' in data:
            topology = data['gnpy-api:topology']
        else:
            raise TopologyError('No topology found in request')
        if 'gnpy-api:equipment' in data:
            equipment = data['gnpy-api:equipment']
        else:
            raise EquipmentError('No equipment found in request')

    return PathRequestService.path_request(topology, equipment, service)
