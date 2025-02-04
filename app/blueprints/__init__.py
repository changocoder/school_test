from flask import Blueprint

from .school import attendance_bp
from .school import classroom_bp
from .school import course_bp
from .school import preceptor_bp
from .school import school_bp
from .school import student_bp
from .school import teacher_bp
from .status import StatusController

# Blueprint principal para la versión de la API
api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")

status_view = StatusController.as_view("status_controller")

# Registramos las rutas de la API
api_v1_bp.add_url_rule("/status", view_func=status_view, methods=["GET"])
api_v1_bp.register_blueprint(school_bp)
api_v1_bp.register_blueprint(teacher_bp)
api_v1_bp.register_blueprint(preceptor_bp)
api_v1_bp.register_blueprint(classroom_bp)
api_v1_bp.register_blueprint(course_bp)
api_v1_bp.register_blueprint(student_bp)
api_v1_bp.register_blueprint(attendance_bp)
