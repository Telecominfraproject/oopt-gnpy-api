#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Esther Le Rouzic
# @Date:   2025-02-03
import json
from pathlib import Path

import pytest
from flask_injector import FlaskInjector

from gnpyapi.core import app
from tests.utils.input import read_json_file


TEST_DATA_DIR = Path(__file__).parent / 'data'
TEST_REQ_DIR_LEGACY = TEST_DATA_DIR / 'req' / 'legacy'
TEST_REQ_DIR = TEST_DATA_DIR / 'req'
TEST_RES_DIR = TEST_DATA_DIR / 'res'

API_VERSION = '/api/v0.2'


@pytest.fixture
def client():
    app.testing = True
    FlaskInjector(app=app)
    with app.test_client() as client:
        yield client


def test_echo(client):
    input_data = read_json_file(TEST_REQ_DIR / "planning_demand_example.json")
    expected_response = read_json_file(TEST_RES_DIR / "planning_demand_res.json")

    response = client.post(f"{API_VERSION}/path-request", json=json.dumps(input_data))
    assert response.status_code == 201
    assert response.get_json() == expected_response


def test_legacy_echo(client):
    input_data = read_json_file(TEST_REQ_DIR_LEGACY / "planning_demand_example.json")
    expected_response = read_json_file(TEST_RES_DIR / "planning_demand_res.json")

    response = client.post(f"{API_VERSION}/path-request", json=input_data)
    assert response.status_code == 201
    assert response.get_json() == expected_response


def test_status(client):
    response = client.get(f"{API_VERSION}/status")
    assert response.status_code == 200
    assert response.get_json() == {"version": "v0.2", "status": "ok"}
