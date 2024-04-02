from flask import jsonify
from flask import request
from flask.views import MethodView

from app.blueprints.exceptions import APIException
from app.schemas.school import ClassroomSchema
from app.schemas.school import CourseSchema
from app.schemas.school import PreceptorSchema
from app.schemas.school import SchoolSchema
from app.schemas.school import TeacherSchema
from app.services.school import ClassroomService
from app.services.school import CourseService
from app.services.school import PreceptorService
from app.services.school import SchoolService
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
