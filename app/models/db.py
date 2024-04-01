import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import UUID
from sqlalchemy.orm import declarative_base

from app.utils import generate_uuid


class _Base:
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    is_deleted = Column(Boolean, default=False)


Base = declarative_base(cls=_Base)
