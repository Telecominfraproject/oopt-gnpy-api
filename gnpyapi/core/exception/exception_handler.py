# coding: utf-8
from http import HTTPStatus
import re

from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from gnpyapi.core.model.error import Error

_reaesc = re.compile(r'\x1b[^m]*m')


def common_error_handler(_request, exception):
    """

    :type exception: Exception

    """
    status_code = 500
    if not isinstance(exception, HTTPException):
        message = HTTPStatus.INTERNAL_SERVER_ERROR.phrase
        description = "Something went wrong on our side."
    else:
        status_code = exception.status_code
        message = HTTPStatus(status_code).phrase
        description = exception.detail
    response = Error(message=message, description=description, code=status_code)

    return JSONResponse(response.__dict__, status_code=status_code)


def bad_request_handler(_request, exception):
    exception_str = " ".join(str(exception).split())
    response = Error(message='bad request', description=_reaesc.sub('', exception_str.replace("\n", " ")),
                     code=400)
    return JSONResponse(response.__dict__, status_code=400)
