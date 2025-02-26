# -*- coding: utf-8 -*-

import logging

from gnpy.tools.worker_utils import designed_network, planning
from gnpy.tools.json_io import results_to_json, load_eqpt_topo_from_json

_logger = logging.getLogger(__name__)


class PathRequestService:

    def __init__(self):
        pass
    @staticmethod
    def path_request(topology: dict, equipment: dict, service: dict = None)->dict:
        (equipment, network) = load_eqpt_topo_from_json(equipment, topology)
        network, _, _ = designed_network(equipment, network)
        # todo parse request
        _, _, _, _, _, result =  planning(network, equipment, service)

        return results_to_json(result)
