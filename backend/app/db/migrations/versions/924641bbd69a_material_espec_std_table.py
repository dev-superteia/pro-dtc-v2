"""material_espec_std_table

Revision ID: 924641bbd69a
Revises: a6ac98d4fa66
Create Date: 2023-01-06 15:03:18.997091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '924641bbd69a'
down_revision = 'a6ac98d4fa66'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_espec_std',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=4), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('tm_material', sa.String(length=9), nullable=False),
        sa.Column('weight', sa.DECIMAL(), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('year'),
        sa.PrimaryKeyConstraint('plant'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('tm_material'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_material_espec_std_composite'), 'material_espec_std', ['year', 'plant', 'material', 'tm_material'])


def downgrade() -> None:
    op.drop_index(op.f('ix_material_espec_std_composite'), table_name='material_espec_std')
    op.drop_table('material_espec_std')
