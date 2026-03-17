# coding: utf-8
from gnpyapi.core import app
from gnpyapi.core import API_VERSION


@app.get(API_VERSION + '/status')
def api_status():
    return {"version": f"{API_VERSION}", "status": "ok"}
