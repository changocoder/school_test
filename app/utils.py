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
    id = Column(String, primary_key=True, default=generate_uuid)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    is_deleted = Column(Boolean, default=False)


Base = declarative_base(cls=_Base)

class BaseMethod(MethodView):
    def __init__(self):
        MethodView.__init__(self)

        if hasattr(current_app, 'services'):
            self.service = current_app.services
