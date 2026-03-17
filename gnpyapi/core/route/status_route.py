# coding: utf-8
from gnpyapi.core import app
from gnpyapi.core import API_VERSION


@app.get(API_VERSION + '/status', status_code=200)
def api_status():
    return {"version": f"{API_VERSION}", "status": "ok"}
