from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class RolePermission(Base):
    __tablename__ = "role_permissions"
    role_id = Column(
        UUID(as_uuid=True),
        ForeignKey("role.id", onupdate='CASCADE', ondelete='SET NULL'),
        primary_key=True,
        nullable=False,
    )
    permission_id = Column(
        UUID(as_uuid=True),
        ForeignKey("permission.id"),
        primary_key=True,
        nullable=False,
    )

    permission = relationship("Permission", lazy="selectin")
    __table_args__ = (
        UniqueConstraint("role_id", "permission_id",
                         name="unique_role_permission"),
    )
