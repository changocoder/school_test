import uuid

from flask import current_app
from flask.views import MethodView


def generate_uuid():
    return str(uuid.uuid4())


def register_resource_routes(bp, view, resource_name):
    bp.add_url_rule(
        "",
        defaults={f"{resource_name}_id": None},
        view_func=view,
        methods=["GET"],
    )
    bp.add_url_rule(
        "",
        view_func=view,
        methods=["POST"],
    )
    bp.add_url_rule(
        f"<string:{resource_name}_id>",
        view_func=view,
        methods=["GET", "PUT", "DELETE"],
    )


class BaseMethod(MethodView):
    def __init__(self):
        MethodView.__init__(self)

        if hasattr(current_app, "services"):
            self.service = current_app.services
