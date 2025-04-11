# coding: utf-8
from gnpyapi.core import app
from gnpyapi.core import API_VERSION


@app.route(API_VERSION + '/status', methods=['GET'])
def api_status():
    return {"version": "v0.1", "status": "ok"}, 200
