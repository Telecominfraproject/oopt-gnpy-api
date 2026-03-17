#!/usr/bin/env python

"""GNPy official API
"""
from fastapi import FastAPI

API_VERSION = "/api/v0.2"

app = FastAPI()

import gnpyapi.core.route.path_request_route  # noqa: E402
import gnpyapi.core.route.status_route  # noqa: F401, E402
