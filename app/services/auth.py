import datetime

from app.config import ConfigClass
from app.runner import jwt


class AuthService:
    @classmethod
    def check_password(cls, password, hashed_password):
        return jwt.check_password_hash(hashed_password, password)

