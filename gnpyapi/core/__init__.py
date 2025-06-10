#!/usr/bin/env python

"""GNPy official API
"""
from flask import Flask

API_VERSION = "/api/v0.2"

app = Flask(__name__)

import gnpyapi.core.route.path_request_route  # noqa: E402
import gnpyapi.core.route.status_route  # noqa: F401, E402
