# -*- coding: utf-8 -*-

import logging

from gnpy.core.exceptions import EquipmentConfigError, NetworkTopologyError
from gnpy.tools.json_io import results_to_json, load_eqpt_topo_from_json
from gnpy.tools.worker_utils import designed_network, planning
from gnpyapi.core.exception.topology_error import TopologyError

from gnpyapi.core.exception.equipment_error import EquipmentError

_logger = logging.getLogger(__name__)


class PathRequestService:

    def __init__(self):
        pass

    @staticmethod
    def path_request(topology: dict, equipment: dict, service: dict = None) -> dict:
        try:
            (equipment, network) = load_eqpt_topo_from_json(equipment, topology)
            network, _, _ = designed_network(equipment, network)
            # todo parse request
            _, _, _, _, _, result = planning(network, equipment, service)
            return results_to_json(result)
        except EquipmentConfigError as e:
            _logger.error(f"An equipment error occurred: {e}")
            raise EquipmentError(str(e))
        except NetworkTopologyError as e:
            _logger.error(f"An equipment error occurred: {e}")
            raise TopologyError(str(e))
        except Exception as e:
            _logger.error(f"An error occurred during path request: {e}")
            raise
