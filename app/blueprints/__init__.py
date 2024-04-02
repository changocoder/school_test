from flask import Blueprint

from .auth.controller import AuthController
from .status import StatusController

# Blueprint principal para la versión de la API
api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")

# Blueprint para la autenticación
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_view = AuthController.as_view("auth_controller")
auth_bp.add_url_rule("/login", view_func=auth_view, methods=["POST"])

status_view = StatusController.as_view("status_controller")

# Registramos las rutas de la API
api_v1_bp.add_url_rule("/status", view_func=status_view, methods=["GET"])
api_v1_bp.register_blueprint(auth_bp)
