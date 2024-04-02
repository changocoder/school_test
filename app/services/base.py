from abc import ABC

from sqlalchemy.exc import SQLAlchemyError

from app.blueprints.exceptions import BadRequestException
from app.blueprints.exceptions import FilterException
from app.blueprints.exceptions import InternalServerErrorException
from app.blueprints.exceptions import NotFoundException
from app.flask_app import db


class GenericService(ABC):
    _model = None
    _session = db.session

    def __init__(self):
        self.model = self._model

    @classmethod
    def get_by_id(cls, _id: str):
        try:
            instance = cls._session.query(cls._model).get(_id)
            if not instance:
                raise NotFoundException(
                    f"{cls._model.__name__} with ID {_id} not found"
                )
            return instance
        except SQLAlchemyError as e:
            raise InternalServerErrorException(f"Error retrieving resource: {str(e)}")

    @classmethod
    def get_all(cls):
        try:
            return cls._session.query(cls._model).all()
        except SQLAlchemyError as e:
            raise InternalServerErrorException(
                f"Error retrieving all resources: {str(e)}"
            )

    @classmethod
    def get_all_by_filter(cls, **kwargs):
        try:
            return cls._session.query(cls._model).filter_by(**kwargs).all()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def get_first_by_filter(cls, **kwargs):
        try:
            return cls._session.query(cls._model).filter_by(**kwargs).first()
        except SQLAlchemyError as e:
            raise FilterException(f"Error in filter operation: {str(e)}")

    @classmethod
    def create(cls, **kwargs):
        try:
            instance = cls._model(**kwargs)
            cls._session.add(instance)
            cls._session.commit()
            return instance
        except SQLAlchemyError as e:
            raise BadRequestException(f"Error creating resource: {str(e)}")

    @classmethod
    def update(cls, _id: str, **kwargs):
        try:
            instance = cls.get_by_id(_id)
            if not instance:
                raise NotFoundException(
                    f"{cls._model.__name__} with ID {_id} not found"
                )
            for key, value in kwargs.items():
                setattr(instance, key, value)
            cls._session.commit()
            return instance
        except SQLAlchemyError as e:
            raise BadRequestException(f"Error updating resource: {str(e)}")

    @classmethod
    def delete(cls, _id: str):
        try:
            instance = cls.get_by_id(_id)
            if not instance:
                raise NotFoundException(
                    f"{cls._model.__name__} with ID {_id} not found"
                )
            instance.is_deleted = True
            cls._session.commit()
            return instance
        except SQLAlchemyError as e:
            raise InternalServerErrorException(f"Error deleting resource: {str(e)}")
