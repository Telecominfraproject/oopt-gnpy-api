# coding: utf-8
import json
from typing import Any, Dict, Union

from fastapi import Body, Depends, status

from gnpy.tools.convert_legacy_yang import yang_to_legacy
from gnpyapi.core import API_VERSION
from gnpyapi.core import app
from gnpyapi.core.exception.equipment_error import EquipmentError
from gnpyapi.core.exception.topology_error import TopologyError
from gnpyapi.core.service.path_request_service import PathRequestService

PATH_REQUEST_BASE_PATH = '/path-request'

RawPayload = Union[Dict[str, Any], str]


def get_path_request_service() -> PathRequestService:
    return PathRequestService()


@app.post(API_VERSION + PATH_REQUEST_BASE_PATH, status_code=status.HTTP_201_CREATED)
def path_request(payload: RawPayload = Body(...), path_request_service: PathRequestService = Depends(get_path_request_service)):
    is_legacy = 'gnpy-api:api' not in payload
    if not is_legacy:
        legacy_data = yang_to_legacy(json.loads(payload))
        service = legacy_data['gnpy-path-computation:services']
        topology = legacy_data['gnpy-network-topology:topology']
        equipment = yang_to_legacy(json.loads(payload)["gnpy-api:api"]['gnpy-eqpt-config:equipment'])
    else:
        data = payload
        service = data['gnpy-api:service']
        if 'gnpy-api:topology' in data:
            topology = data['gnpy-api:topology']
        else:
            raise TopologyError('No topology found in request')
        if 'gnpy-api:equipment' in data:
            equipment = data['gnpy-api:equipment']
        else:
            raise EquipmentError('No equipment found in request')

    return path_request_service.path_request(topology, equipment, service)
