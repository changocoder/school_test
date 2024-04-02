from flask import jsonify
from flask.views import MethodView


class StatusController(MethodView):
    def get(self):
        return jsonify({"status": "ok"})
