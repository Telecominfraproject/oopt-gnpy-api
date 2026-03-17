#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
gnpy.tools.rest_example
=======================

GNPy as a rest API example
'''

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

import uvicorn
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gnpyapi.core import app  # noqa: E402
from gnpyapi.core.exception.equipment_error import EquipmentError  # noqa: E402
from gnpyapi.core.exception.exception_handler import bad_request_handler, common_error_handler  # noqa: E402
from gnpyapi.core.exception.path_computation_error import PathComputationError  # noqa: E402
from gnpyapi.core.exception.topology_error import TopologyError  # noqa: E402

_logger = logging.getLogger(__name__)


def _init_logger():
    handler = RotatingFileHandler('api.log', maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
    ch = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, handlers=[handler, ch],
                        format="%(asctime)s %(levelname)s %(name)s(%(lineno)s) [%(threadName)s - %(thread)d] - %("
                               "message)s")


def _init_app():
    for error in (KeyError, TypeError, ValueError, AssertionError, TopologyError, EquipmentError,
                  PathComputationError, RequestValidationError):
        app.add_exception_handler(error, bad_request_handler)

    app.add_exception_handler(HTTPException, common_error_handler)


def main():
    _init_logger()
    _init_app()
    uvicorn.run(app, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
