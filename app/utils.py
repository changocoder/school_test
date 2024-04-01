import uuid

from flask import current_app
from flask.views import MethodView


def generate_uuid():
    return str(uuid.uuid4())


class BaseMethod(MethodView):
    def __init__(self):
        MethodView.__init__(self)

        if hasattr(current_app, "services"):
            self.service = current_app.services
