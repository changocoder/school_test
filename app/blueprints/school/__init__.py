from flask import Blueprint

from .school_controller import AttendanceController
from .school_controller import ClassroomController
from .school_controller import CourseController
from .school_controller import EnrollStudentController
from .school_controller import PreceptorController
from .school_controller import SchoolController
from .school_controller import StudentController
from .school_controller import TeacherController
from app.utils import register_resource_routes

# Blueprint para la School API
school_bp = Blueprint("school", __name__, url_prefix="/school/")
teacher_bp = Blueprint("teacher", __name__, url_prefix="/teacher/")
preceptor_bp = Blueprint("preceptor", __name__, url_prefix="/preceptor/")
classroom_bp = Blueprint("classroom", __name__, url_prefix="/classroom/")
course_bp = Blueprint("course", __name__, url_prefix="/course/")
student_bp = Blueprint("student", __name__, url_prefix="/student/")
attendance_bp = Blueprint("attendance", __name__, url_prefix="/attendance/")

# Vistas de la API
school_view = SchoolController.as_view("school_controller")
teacher_view = TeacherController.as_view("teacher_controller")
preceptor_view = PreceptorController.as_view("preceptor_controller")
classroom_view = ClassroomController.as_view("classroom_controller")
course_view = CourseController.as_view("course_controller")
student_view = StudentController.as_view("student_controller")
enroll_student_view = EnrollStudentController.as_view("enroll_student_controller")
attendance_view = AttendanceController.as_view("attendance_controller")

# Custom routes
course_bp.add_url_rule(
    "/enroll-student",
    view_func=enroll_student_view,
    methods=[
        "POST",
    ],
)

# Registramos las rutas de la API
register_resource_routes(school_bp, school_view, "school")
register_resource_routes(teacher_bp, teacher_view, "teacher")
register_resource_routes(preceptor_bp, preceptor_view, "preceptor")
register_resource_routes(classroom_bp, classroom_view, "classroom")
register_resource_routes(course_bp, course_view, "course")
register_resource_routes(student_bp, student_view, "student")
register_resource_routes(attendance_bp, attendance_view, "attendance")
