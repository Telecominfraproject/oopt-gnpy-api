#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Esther Le Rouzic
# @Date:   2025-02-03
import json
from pathlib import Path

import pytest
from gnpyapi.core.exception.equipment_error import EquipmentError

from gnpyapi.core.service.path_request_service import PathRequestService
from gnpyapi.core.exception.topology_error import TopologyError

TEST_DATA_DIR = Path(__file__).parent.parent / 'data'
TEST_REQ_DIR = TEST_DATA_DIR / 'req'
TEST_RES_DIR = TEST_DATA_DIR / 'res'


def read_json_file(path):
    with open(path, "r") as file:
        return json.load(file)


def test_path_request_success():
    input_data = read_json_file(TEST_REQ_DIR / "planning_demand_example.json")
    expected_response = read_json_file(TEST_RES_DIR / "planning_demand_res.json")
    topology = input_data["gnpy-api:topology"]
    equipment = input_data["gnpy-api:equipment"]
    service = input_data["gnpy-api:service"]

    result = PathRequestService.path_request(topology, equipment, service)
    assert result == expected_response


def test_path_request_invalid_equipment():
    input_data = read_json_file(TEST_REQ_DIR / "planning_demand_wrong_eqpt.json")
    topology = input_data["gnpy-api:topology"]
    equipment = input_data["gnpy-api:equipment"]
    service = input_data["gnpy-api:service"]

    with pytest.raises(EquipmentError) as exc:
        PathRequestService.path_request(topology, equipment, service)
    assert "invalid" in str(exc.value).lower()
    assert "deltap" in str(exc.value).lower()


def test_path_request_invalid_topology():
    input_data = read_json_file(TEST_REQ_DIR / "planning_demand_wrong_topology.json")
    topology = input_data["gnpy-api:topology"]
    equipment = input_data["gnpy-api:equipment"]
    service = input_data["gnpy-api:service"]

    with pytest.raises(TopologyError) as exc:
        PathRequestService.path_request(topology, equipment, service)
    assert "can not find" in str(exc.value).lower()
