from sqlalchemy import Column, String, Boolean

from app.model.db import Base


class User(Base):
    __tablename__ = "user"

    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_active = Column(String)
    is_admin = Column(Boolean)