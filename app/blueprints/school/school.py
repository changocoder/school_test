from flask import jsonify
from flask import request
from flask.views import MethodView

from app.blueprints.exceptions import APIException
from app.schemas.school import SchoolSchema
from app.services.school import SchoolService


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
