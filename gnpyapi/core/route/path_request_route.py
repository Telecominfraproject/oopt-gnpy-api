# coding: utf-8
import json

from flask import request

from gnpyapi.core import app
from gnpyapi.core.exception.equipment_error import EquipmentError
from gnpyapi.core.exception.topology_error import TopologyError
from gnpyapi.core.service.path_request_service import PathRequestService
from gnpy.tools.convert_legacy_yang import yang_to_legacy
from gnpyapi.core import API_VERSION

PATH_REQUEST_BASE_PATH = '/path-request'


@app.route(API_VERSION + PATH_REQUEST_BASE_PATH, methods=['POST'])
def path_request(path_request_service: PathRequestService):
    is_legacy = 'gnpy-api:api' not in request.json
    if not is_legacy:
        legacy_data = yang_to_legacy(json.loads(request.json))
        service = legacy_data['gnpy-path-computation:services']
        topology = legacy_data['gnpy-network-topology:topology']
        equipment = yang_to_legacy(json.loads(request.json)["gnpy-api:api"]['gnpy-eqpt-config:equipment'])
    else:
        data = request.json
        service = data['gnpy-api:service']
        if 'gnpy-api:topology' in data:
            topology = data['gnpy-api:topology']
        else:
            raise TopologyError('No topology found in request')
        if 'gnpy-api:equipment' in data:
            equipment = data['gnpy-api:equipment']
        else:
            raise EquipmentError('No equipment found in request')

    return path_request_service.path_request(topology, equipment, service), 201
