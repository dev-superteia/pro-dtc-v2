import datetime
from uuid import uuid4
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID


class Permission(Base):
    __tablename__ = "permission"
    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    name = Column(String(100), index=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
