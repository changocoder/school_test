import datetime
import uuid
from abc import ABC
from typing import Type

from flask import current_app
from flask.views import MethodView
from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from app.extension import db


def generate_uuid():
    return str(uuid.uuid4())


class _Base:
    id = Column(String, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    is_deleted = Column(Boolean, default=False)


Base = declarative_base(cls=_Base)


class GenericService(ABC):
    _model = None
    _session = db.session

    def __init__(self):
        self.model = self._model

    @classmethod
    def get_by_id(cls, _id: str):
        return cls._session.query(cls._model).get(_id)

    @classmethod
    def get_all(cls):
        return cls._session.query(cls._model).all()

    @classmethod
    def create(cls, **kwargs):
        instance = cls._model(**kwargs)
        cls._session.add(instance)
        cls._session.commit()
        return instance

    @classmethod
    def update(cls, _id: str, **kwargs):
        instance = cls.get_by_id(_id)
        for key, value in kwargs.items():
            setattr(instance, key, value)
        cls._session.commit()
        return instance

    @classmethod
    def delete(cls, _id: str):
        instance = cls.get_by_id(_id)
        instance.is_deleted = True
        cls._session.commit()
        return instance


class BaseMethod(MethodView):
    def __init__(self):
        MethodView.__init__(self)

        if hasattr(current_app, 'services'):
            self.service = current_app.services
