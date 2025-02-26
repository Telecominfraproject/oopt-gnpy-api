#!/usr/bin/env python

"""GNPy official API
"""
from flask import Flask

app = Flask(__name__)

import gnpyapi.core.route.path_request_route
import gnpyapi.core.route.status_route
