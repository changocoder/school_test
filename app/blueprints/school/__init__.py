from flask import Blueprint

from .school import ClassroomController
from .school import CourseController
from .school import PreceptorController
from .school import SchoolController
from .school import TeacherController
from app.utils import register_resource_routes

# Blueprint para la School API
school_bp = Blueprint("school", __name__, url_prefix="/school")
teacher_bp = Blueprint("teacher", __name__, url_prefix="/teacher")
preceptor_bp = Blueprint("preceptor", __name__, url_prefix="/preceptor")
classroom_bp = Blueprint("classroom", __name__, url_prefix="/classroom")
course_bp = Blueprint("course", __name__, url_prefix="/course")

school_view = SchoolController.as_view("school_controller")
teacher_view = TeacherController.as_view("teacher_controller")
preceptor_view = PreceptorController.as_view("preceptor_controller")
classroom_view = ClassroomController.as_view("classroom_controller")
course_view = CourseController.as_view("course_controller")

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

register_resource_routes(teacher_bp, teacher_view, "teacher")
register_resource_routes(preceptor_bp, preceptor_view, "preceptor")
register_resource_routes(classroom_bp, classroom_view, "classroom")
register_resource_routes(course_bp, course_view, "course")
