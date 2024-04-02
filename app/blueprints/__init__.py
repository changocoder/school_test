from flask import Blueprint

from .school import school_bp
from .status import StatusController

# Blueprint principal para la versión de la API
api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")

status_view = StatusController.as_view("status_controller")

# Registramos las rutas de la API
api_v1_bp.add_url_rule("/status", view_func=status_view, methods=["GET"])
api_v1_bp.register_blueprint(school_bp)
