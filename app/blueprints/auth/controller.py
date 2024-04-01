from flask.views import MethodView
from flask import request, jsonify

from app.services.user import UserService


class AuthController(MethodView):
    user_service = UserService()

    def post(self):
        data = request.get_json()
        result = self.user_service.check_password(

        )



