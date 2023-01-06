"""material_espec_zp88_table

Revision ID: 856f12f539e8
Revises: bfba9232f3b6
Create Date: 2023-01-06 16:52:28.645155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '856f12f539e8'
down_revision = 'bfba9232f3b6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_espec_zp88',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=4), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('document', sa.String(length=20), nullable=False),
        sa.Column('utilization', sa.String(length=20), nullable=False),
        sa.Column('charge', sa.DECIMAL(), nullable=False),
        sa.Column('quote', sa.Integer(), nullable=False),
        sa.Column('charge_utilization', sa.DECIMAL(), nullable=False),
        sa.Column('recycle', sa.String(length=20), nullable=False),
        sa.Column('total_recycle', sa.DECIMAL(), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('time', sa.DECIMAL(), nullable=False),
        sa.Column('machine', sa.String(length=20), nullable=False),
        sa.Column('dens_theor', sa.DECIMAL(), nullable=False),
        sa.Column('dens_real', sa.DECIMAL(), nullable=False),
        sa.Column('dt_phase', sa.TIMESTAMP(), nullable=False),
        sa.Column('dt_creation', sa.TIMESTAMP(), nullable=False),
        sa.Column('dt_release', sa.TIMESTAMP(), nullable=False),
        sa.Column('dt_expir', sa.TIMESTAMP(), nullable=False),
        sa.Column('rpm', sa.Integer(), nullable=False),
        sa.Column('time_effect', sa.Integer(), nullable=False),
        sa.Column('DT_PHASEOUT', sa.Integer(), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('plant'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('document'),
        sa.PrimaryKeyConstraint('utilization'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_material_espec_zp88_composite'), 'material_espec_zp88', ['plant', 'material', 'document', 'utilization'])


def downgrade() -> None:
    op.drop_index(op.f('ix_material_espec_zp88_composite'), table_name='material_espec_zp88')
    op.drop_table('material_espec_zp88')
