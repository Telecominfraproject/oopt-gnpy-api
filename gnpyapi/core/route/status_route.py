# coding: utf-8
from gnpyapi.core import app


@app.route('/api/v1/status', methods=['GET'])
def api_status():
    return {"version": "v1", "status": "ok"}, 200
