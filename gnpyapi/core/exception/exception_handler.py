# coding: utf-8
import re
from http import HTTPStatus

from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from gnpyapi.core.exception.equipment_error import EquipmentError
from gnpyapi.core.exception.path_computation_error import PathComputationError
from gnpyapi.core.exception.topology_error import TopologyError
from gnpyapi.core.model.error import Error

_reaesc = re.compile(r'\x1b[^m]*m')


def common_error_handler(request: Request, exception):
    status_code = 500
    if not isinstance(exception, StarletteHTTPException):
        message = "Internal Server Error"
        description = "Something went wrong on our side."
    else:
        status_code = exception.status_code
        try:
            message = HTTPStatus(status_code).phrase
        except ValueError:
            message = "HTTP Error"
        description = exception.detail
    response = Error(message=message, description=description, code=status_code)
    return JSONResponse(content=response.__dict__, status_code=status_code)


def bad_request_handler(request: Request, exception):
    exception_str = " ".join(str(exception).split())
    response = Error(message='bad request', description=_reaesc.sub('', exception_str.replace("\n", " ")),
                     code=400)
    return JSONResponse(content=response.__dict__, status_code=400)


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(KeyError, bad_request_handler)
    app.add_exception_handler(TypeError, bad_request_handler)
    app.add_exception_handler(ValueError, bad_request_handler)
    app.add_exception_handler(AssertionError, bad_request_handler)
    app.add_exception_handler(TopologyError, bad_request_handler)
    app.add_exception_handler(EquipmentError, bad_request_handler)
    app.add_exception_handler(PathComputationError, bad_request_handler)
    app.add_exception_handler(RequestValidationError, bad_request_handler)
    app.add_exception_handler(StarletteHTTPException, common_error_handler)
    app.add_exception_handler(Exception, common_error_handler)
