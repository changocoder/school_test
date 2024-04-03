from flask import jsonify
from flask import request
from flask.views import MethodView

from app.blueprints.exceptions import APIException
from app.schemas.school import AttendanceDumpSchema
from app.schemas.school import AttendanceSchema
from app.schemas.school import ClassroomSchema
from app.schemas.school import CourseSchema
from app.schemas.school import EnrollStudentSchema
from app.schemas.school import PreceptorSchema
from app.schemas.school import SchoolSchema
from app.schemas.school import StudentSchema
from app.schemas.school import TeacherSchema
from app.services.school import AttendanceService
from app.services.school import ClassroomService
from app.services.school import CourseService
from app.services.school import PreceptorService
from app.services.school import SchoolService
from app.services.school import StudentService
from app.services.school import TeacherService


class SchoolController(MethodView):
    service = SchoolService()
    schema = SchoolSchema()

    def get(self, school_id=None):
        try:
            if school_id:
                school = self.service.get_by_id(school_id)
                return jsonify(self.schema.dump(school))
            else:
                schools = self.service.get_all()
                return jsonify(self.schema.dump(schools, many=True))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def post(self):
        try:
            school_data = self.schema.load(request.json)
            new_school = self.service.create(**school_data)
            return jsonify(self.schema.dump(new_school)), 201
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def put(self, school_id):
        try:
            school_data = self.schema.load(request.json)
            updated_school = self.service.update(school_id, **school_data)
            return jsonify(self.schema.dump(updated_school))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def delete(self, school_id):
        try:
            self.service.delete(school_id)
            return jsonify({}), 204
        except APIException as e:
            return jsonify({"error": e.description}), e.code


class TeacherController(MethodView):
    service = TeacherService()
    schema = TeacherSchema()

    def get(self, teacher_id=None):
        try:
            if teacher_id:
                teacher = self.service.get_by_id(teacher_id)
                return jsonify(self.schema.dump(teacher))
            else:
                teachers = self.service.get_all()
                return jsonify(self.schema.dump(teachers, many=True))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def post(self):
        try:
            teacher_data = self.schema.load(request.json)
            new_teacher = self.service.create(**teacher_data)
            return jsonify(self.schema.dump(new_teacher)), 201
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def put(self, teacher_id):
        try:
            teacher_data = self.schema.load(request.json)
            updated_teacher = self.service.update(teacher_id, **teacher_data)
            return jsonify(self.schema.dump(updated_teacher))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def delete(self, teacher_id):
        try:
            self.service.delete(teacher_id)
            return jsonify({}), 204
        except APIException as e:
            return jsonify({"error": e.description}), e.code


class PreceptorController(MethodView):
    service = PreceptorService()
    schema = PreceptorSchema()

    def get(self, preceptor_id=None):
        try:
            if preceptor_id:
                preceptor = self.service.get_by_id(preceptor_id)
                return jsonify(self.schema.dump(preceptor))
            else:
                preceptors = self.service.get_all()
                return jsonify(self.schema.dump(preceptors, many=True))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def post(self):
        try:
            preceptor_data = self.schema.load(request.json)
            new_preceptor = self.service.create(**preceptor_data)
            return jsonify(self.schema.dump(new_preceptor)), 201
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def put(self, preceptor_id):
        try:
            preceptor_data = self.schema.load(request.json)
            updated_preceptor = self.service.update(preceptor_id, **preceptor_data)
            return jsonify(self.schema.dump(updated_preceptor))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def delete(self, preceptor_id):
        try:
            self.service.delete(preceptor_id)
            return jsonify({}), 204
        except APIException as e:
            return jsonify({"error": e.description}), e.code


class ClassroomController(MethodView):
    service = ClassroomService()
    schema = ClassroomSchema()

    def get(self, classroom_id=None):
        try:
            if classroom_id:
                classroom = self.service.get_by_id(classroom_id)
                return jsonify(self.schema.dump(classroom))
            else:
                classrooms = self.service.get_all()
                return jsonify(self.schema.dump(classrooms, many=True))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def post(self):
        try:
            classroom_data = self.schema.load(request.json)
            new_classroom = self.service.create(**classroom_data)
            return jsonify(self.schema.dump(new_classroom)), 201
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def put(self, classroom_id):
        try:
            classroom_data = self.schema.load(request.json)
            updated_classroom = self.service.update(classroom_id, **classroom_data)
            return jsonify(self.schema.dump(updated_classroom))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def delete(self, classroom_id):
        try:
            self.service.delete(classroom_id)
            return jsonify({}), 204
        except APIException as e:
            return jsonify({"error": e.description}), e.code


class CourseController(MethodView):
    service = CourseService()
    schema = CourseSchema()

    def get(self, course_id=None):
        try:
            if course_id:
                course = self.service.get_by_id(course_id)
                return jsonify(self.schema.dump(course))
            else:
                courses = self.service.get_all()
                return jsonify(self.schema.dump(courses, many=True))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def post(self):
        try:
            course_data = self.schema.load(request.json)
            new_course = self.service.create(**course_data)
            return jsonify(self.schema.dump(new_course)), 201
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def put(self, course_id):
        try:
            course_data = self.schema.load(request.json)
            updated_course = self.service.update(course_id, **course_data)
            return jsonify(self.schema.dump(updated_course))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def delete(self, course_id):
        try:
            self.service.delete(course_id)
            return jsonify({}), 204
        except APIException as e:
            return jsonify({"error": e.description}), e.code


class StudentController(MethodView):
    service = StudentService()
    schema = StudentSchema()

    def get(self, student_id=None):
        try:
            if student_id:
                student = self.service.get_by_id(student_id)
                return jsonify(self.schema.dump(student))
            else:
                students = self.service.get_all()
                return jsonify(self.schema.dump(students, many=True))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def post(self):
        try:
            student_data = self.schema.load(request.json)
            new_student = self.service.create(**student_data)
            return jsonify(self.schema.dump(new_student)), 201
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def put(self, student_id):
        try:
            student_data = self.schema.load(request.json)
            updated_student = self.service.update(student_id, **student_data)
            return jsonify(self.schema.dump(updated_student))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def delete(self, student_id):
        try:
            self.service.delete(student_id)
            return jsonify({}), 204
        except APIException as e:
            return jsonify({"error": e.description}), e.code


class EnrollStudentController(MethodView):
    course_service = CourseService()
    student_service = StudentService()
    schema = EnrollStudentSchema()

    def post(self):
        try:
            data_enroll = self.schema.load(request.json)

            self.course_service.enroll_student(data_enroll)

            return jsonify({"message": "Student enrolled successfully"}), 204
        except APIException as e:
            return jsonify({"error": e.description}), e.code


class AttendanceController(MethodView):
    attendance_service = AttendanceService()
    schema = AttendanceSchema()
    dump_schema = AttendanceDumpSchema()

    def post(self):
        try:
            attendance_data = self.schema.load(request.json)
            new_attendance = self.attendance_service.create_attendace_and_detail(
                attendance_data
            )
            return jsonify(self.schema.dump(new_attendance)), 201
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def get(self, attendance_id=None):
        try:
            if attendance_id:
                attendance = self.attendance_service.get_by_id(attendance_id)
                return jsonify(self.schema.dump(attendance))
            else:
                attendances = self.attendance_service.get_all()
                return jsonify(self.schema.dump(attendances, many=True))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def put(self, attendance_id):
        try:
            attendance_data = self.schema.load(request.json)
            updated_attendance = self.attendance_service.update(
                attendance_id, **attendance_data
            )
            return jsonify(self.schema.dump(updated_attendance))
        except APIException as e:
            return jsonify({"error": e.description}), e.code

    def delete(self, attendance_id):
        try:
            self.attendance_service.delete(attendance_id)
            return jsonify({}), 204
        except APIException as e:
            return jsonify({"error": e.description}), e.code
