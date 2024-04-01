from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from werkzeug.security import generate_password_hash

from app.models.db import Base


class User(Base):
    __tablename__ = "users"

    name = Column(String(128))
    last_name = Column(String(128))
    email = Column(String(128), unique=True)
    username = Column(String(128), unique=True)
    password = Column(String(255))
    is_active = Column(Boolean)
    is_admin = Column(Boolean)

    def set_password(self, password):
        self.password = generate_password_hash(password)
