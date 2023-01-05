"""create permission table

Revision ID: 6d5ebb85f6c1
Revises: 2081214b4192
Create Date: 2022-11-14 01:14:19.301310

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6d5ebb85f6c1'
down_revision = '2081214b4192'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "permission",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_permissions_id"), "permission",
                    ["id"], unique=False)
    op.create_index(op.f("ix_permissions_name"), 
                    "permission", ["name"], unique=False)
    op.create_table(
        "role_permissions",
        sa.Column("permission_id", postgresql.UUID(as_uuid=True),
                  nullable=False),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(["role_id"], ["role.id"],),
        sa.ForeignKeyConstraint(["permission_id"], ["permission.id"],),
        sa.PrimaryKeyConstraint("permission_id", "role_id"),
        sa.UniqueConstraint("role_id", "permission_id",
                            name="unique_role_permission"),
    )


def downgrade() -> None:
    op.drop_table("role_permissions")
    op.drop_index(op.f("ix_permissions_name"), table_name="permission")
    op.drop_index(op.f("ix_permissions_id"), table_name="permission")
    op.drop_table("permission")
