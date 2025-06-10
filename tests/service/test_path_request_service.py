#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Esther Le Rouzic
# @Date:   2025-02-03
from pathlib import Path

from gnpy.tools.convert_legacy_yang import yang_to_legacy

from gnpyapi.core.service.path_request_service import PathRequestService
from tests.utils.input import read_json_file

TEST_DATA_DIR = Path(__file__).parent.parent / 'data'
TEST_REQ_DIR = TEST_DATA_DIR / 'req'
TEST_REQ_DIR_LEGACY = TEST_DATA_DIR / 'req' / 'legacy'
TEST_RES_DIR = TEST_DATA_DIR / 'res'


def test_path_request_success():
    input_data = read_json_file(TEST_REQ_DIR / "planning_demand_example.json")
    expected_response = read_json_file(TEST_RES_DIR / "planning_demand_res.json")
    input_data = input_data["gnpy-api:api"]
    topology = yang_to_legacy(input_data["gnpy-network-topology:topology"])
    equipment = yang_to_legacy(input_data["gnpy-eqpt-config:equipment"])
    service = yang_to_legacy(input_data["gnpy-path-computation:services"])

    result = PathRequestService.path_request(topology, equipment, service)
    assert result == expected_response


def test_legacy_path_request_success():
    input_data = read_json_file(TEST_REQ_DIR_LEGACY / "planning_demand_example.json")
    expected_response = read_json_file(TEST_RES_DIR / "planning_demand_res.json")
    topology = input_data["gnpy-api:topology"]
    equipment = input_data["gnpy-api:equipment"]
    service = input_data["gnpy-api:service"]

    result = PathRequestService.path_request(
        topology=topology,
        equipment=equipment,
        service=service)
    assert result == expected_response
