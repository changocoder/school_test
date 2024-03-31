import datetime

from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


class _Base:
    id = Column(String, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    is_deleted = Column(Boolean, default=False)


Base = declarative_base(cls=_Base)

