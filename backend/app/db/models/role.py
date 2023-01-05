import datetime
from uuid import uuid4
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class Role(Base):
    __tablename__ = "role"
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
    role_permission = relationship("RolePermission", lazy="selectin",
                                   cascade="all,delete")
