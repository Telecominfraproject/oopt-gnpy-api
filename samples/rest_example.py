#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
gnpy.tools.rest_example
=======================

GNPy as a rest API example
'''

import logging
from logging.handlers import RotatingFileHandler

import werkzeug
from flask_injector import FlaskInjector

from gnpyapi.core import app
from gnpyapi.core.exception.equipment_error import EquipmentError
from gnpyapi.core.exception.exception_handler import bad_request_handler, common_error_handler
from gnpyapi.core.exception.path_computation_error import PathComputationError
from gnpyapi.core.exception.topology_error import TopologyError
import argparse

_logger = logging.getLogger(__name__)


def _init_logger():
    handler = RotatingFileHandler('api.log', maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
    ch = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, handlers=[handler, ch],
                        format="%(asctime)s %(levelname)s %(name)s(%(lineno)s) [%(threadName)s - %(thread)d] - %("
                               "message)s")


def _init_app():
    app.register_error_handler(KeyError, bad_request_handler)
    app.register_error_handler(TypeError, bad_request_handler)
    app.register_error_handler(ValueError, bad_request_handler)
    # app.register_error_handler(exceptions.ConfigurationError, bad_request_handler)
    # app.register_error_handler(exceptions.DisjunctionError, bad_request_handler)
    # app.register_error_handler(exceptions.EquipmentConfigError, bad_request_handler)
    # app.register_error_handler(exceptions.NetworkTopologyError, bad_request_handler)
    # app.register_error_handler(exceptions.ServiceError, bad_request_handler)
    # app.register_error_handler(exceptions.SpectrumError, bad_request_handler)
    # app.register_error_handler(exceptions.ParametersError, bad_request_handler)
    app.register_error_handler(AssertionError, bad_request_handler)
    # app.register_error_handler(InternalServerError, common_error_handler)
    app.register_error_handler(TopologyError, bad_request_handler)
    app.register_error_handler(EquipmentError, bad_request_handler)

    app.register_error_handler(PathComputationError, bad_request_handler)
    for error_code in werkzeug.exceptions.default_exceptions:
        app.register_error_handler(error_code, common_error_handler)


def main(http: bool = False):
    _init_logger()
    _init_app()
    FlaskInjector(app=app)

    if http:
        app.run(host='0.0.0.0', port=8080)
    else:
        app.run(host='0.0.0.0', port=8080, ssl_context='adhoc')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rest API example")

    parser.add_argument("--http", action="store_true", help="run server with http instead of https")

    args = parser.parse_args()

    main(http=args.http)
