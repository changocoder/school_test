from http import HTTPStatus

from flask import jsonify
from flask import request
from marshmallow import ValidationError

from app.schemas.user import UserSchema
from app.services.user import UserService
from app.utils import BaseMethod


class UserController(BaseMethod):
    user_service = UserService()
    schema = UserSchema()

    def get(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if user:
            return jsonify(self.schema.dump(user))
        return jsonify({}), HTTPStatus.NOT_FOUND

    def post(self):
        try:
            user = self.schema.load(request.json)
        except ValidationError as e:
            return jsonify(e.messages), HTTPStatus.BAD_REQUEST

        user = self.user_service.create(**user)

        return jsonify(self.schema.dump(user)), HTTPStatus.CREATED

    def put(self, user_id):
        try:
            user = self.schema.load(request.json)
        except ValidationError as e:
            return jsonify(e.messages), HTTPStatus.BAD_REQUEST

        user = self.user_service.update(user_id, **user)

        return jsonify(self.schema.dump(user)), HTTPStatus.OK

    def delete(self, user_id):
        user = self.user_service.delete(user_id)
        return jsonify(self.schema.dump(user)), HTTPStatus.OK

    def get_all(self):
        users = self.user_service.get_all()
        return jsonify(self.schema.dump(users, many=True)), HTTPStatus.OK
