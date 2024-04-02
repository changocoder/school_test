from flask import Blueprint

from .school import SchoolController

# Blueprint para la School API
school_bp = Blueprint("school", __name__, url_prefix="/school")
school_view = SchoolController.as_view("school_controller")

# Registramos las rutas de la API
school_bp.add_url_rule(
    "",
    defaults={"school_id": None},
    view_func=school_view,
    methods=[
        "GET",
    ],
)
school_bp.add_url_rule(
    "",
    view_func=school_view,
    methods=[
        "POST",
    ],
)
school_bp.add_url_rule(
    "/<string:school_id>", view_func=school_view, methods=["GET", "PUT", "DELETE"]
)
