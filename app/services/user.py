from app.models.user import User
from app.services.base import GenericService

from werkzeug.security import check_password_hash


class UserService(GenericService):
    _model = User

    @classmethod
    def check_password(cls, user, password):
        return check_password_hash(user.password, password)
