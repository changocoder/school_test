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


class BaseMethod(MethodView):
    def __init__(self):
        MethodView.__init__(self)

        if hasattr(current_app, 'services'):
            self.service = current_app.services
