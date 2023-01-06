"""material_espec_zp45_table

Revision ID: 8ccaaea68ffe
Revises: 140955525fe4
Create Date: 2023-01-06 16:43:27.194282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ccaaea68ffe'
down_revision = '140955525fe4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_espec_zp45',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=4), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('component', sa.String(length=9), nullable=False),
        sa.Column('document', sa.String(length=20), nullable=True),
        sa.Column('subclass', sa.String(length=4), nullable=True),
        sa.Column('cost_center', sa.String(length=4), nullable=True),
        sa.Column('workcenter', sa.String(length=4), nullable=True),
        sa.Column('team', sa.DECIMAL(), nullable=True),
        sa.Column('quote', sa.Integer(), nullable=True),
        sa.Column('utilization', sa.DECIMAL(), nullable=True),
        sa.Column('measure_unit', sa.String(length=3), nullable=True),
        sa.Column('labor_main', sa.DECIMAL(), nullable=True),
        sa.Column('labor_auxiliary', sa.DECIMAL(), nullable=True),
        sa.Column('increase', sa.DECIMAL(), nullable=True),
        sa.Column('cycle', sa.DECIMAL(), nullable=True),
        sa.Column('expenditure', sa.DECIMAL(), nullable=True),
        sa.Column('family', sa.String(length=2), nullable=True),
        sa.Column('weight', sa.DECIMAL(), nullable=True),
        sa.Column('measure_weight', sa.String(length=3), nullable=True),
        sa.Column('qtd_without', sa.DECIMAL(), nullable=True),
        sa.Column('labor_main_base', sa.DECIMAL(), nullable=True),
        sa.Column('labor_auxiliary_base', sa.DECIMAL(), nullable=True),
        sa.Column('increase_base', sa.DECIMAL(), nullable=True),
        sa.Column('cycle_base', sa.DECIMAL(), nullable=True),
        sa.Column('expenditure_base', sa.DECIMAL(), nullable=True),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('plant'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('component'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_material_espec_zp45_composite'), 'material_espec_zp45', ['plant', 'material', 'component'])


def downgrade() -> None:
    op.drop_index(op.f('ix_material_espec_zp45_composite'), table_name='material_espec_zp45')
    op.drop_table('material_espec_zp45')
    