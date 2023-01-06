"""material_cost_table

Revision ID: a6ac98d4fa66
Revises: c6e06203b539
Create Date: 2023-01-06 15:00:13.995879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6ac98d4fa66'
down_revision = 'c6e06203b539'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_cost',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('description', sa.String(length=200), nullable=True),
        sa.Column('cost_std', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m01', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m02', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m03', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m04', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m05', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m06', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m07', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m08', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m09', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m10', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m11', sa.DECIMAL(), nullable=False),
        sa.Column('cost_m12', sa.DECIMAL(), nullable=False),
        sa.Column('cost_b01', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b02', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b03', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b04', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b05', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b06', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b07', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b08', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b09', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b10', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b11', sa.DECIMAL(), nullable=True),
        sa.Column('cost_b12', sa.DECIMAL(), nullable=True),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('year'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_material_cost_composite'), 'material_cost', ['year', 'material'])

def downgrade() -> None:
    op.drop_index(op.f('ix_material_cost_composite'), table_name='material_cost')
    op.drop_table('material_cost')
