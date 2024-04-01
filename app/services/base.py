from abc import ABC

from app.extension import db


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
    def get_all_by_filter(cls, **kwargs):
        return cls._session.query(cls._model).filter_by(**kwargs).all()

    @classmethod
    def get_first_by_filter(cls, **kwargs):
        return cls._session.query(cls._model).filter_by(**kwargs).first()

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
