"""material_volum_table

Revision ID: f1fd6586d661
Revises: 856f12f539e8
Create Date: 2023-01-06 16:54:14.883849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1fd6586d661'
down_revision = '856f12f539e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_volum',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=4), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('month', sa.Integer(), nullable=False),
        sa.Column('dt_datetime', sa.TIMESTAMP(), nullable=False),
        sa.Column('warehouse', sa.String(length=4), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('total_volum', sa.Integer(), nullable=False),
        sa.Column('total_value', sa.DECIMAL(), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('plant'),
        sa.PrimaryKeyConstraint('year'),
        sa.PrimaryKeyConstraint('month'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_material_volum_composite'), 'material_volum', ['plant', 'year', 'month', 'material'])


def downgrade() -> None:
    op.drop_index(op.f('ix_material_volum_composite'), table_name='material_volum')
    op.drop_table('material_volum')
