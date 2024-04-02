import uuid

from flask import current_app
from flask.views import MethodView


def generate_uuid():
    return str(uuid.uuid4())


def register_api(view, endpoint, url, pk="id", pk_type="str"):
    view_func = view.as_view(endpoint)
    current_app.add_url_rule(
        url,
        defaults={pk: None},
        view_func=view_func,
        methods=[
            "GET",
        ],
    )
    current_app.add_url_rule(
        url,
        view_func=view_func,
        methods=[
            "POST",
        ],
    )
    current_app.add_url_rule(
        f"{url}<{pk_type}:{pk}>",
        view_func=view_func,
        methods=["GET", "PUT", "DELETE"],
    )


class BaseMethod(MethodView):
    def __init__(self):
        MethodView.__init__(self)

        if hasattr(current_app, "services"):
            self.service = current_app.services
