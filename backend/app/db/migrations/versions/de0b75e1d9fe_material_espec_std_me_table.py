"""material_espec_std_me_table

Revision ID: de0b75e1d9fe
Revises: 924641bbd69a
Create Date: 2023-01-06 15:04:51.829613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de0b75e1d9fe'
down_revision = '924641bbd69a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_espec_std_me',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=4), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('espec', sa.String(length=20), nullable=False),
        sa.Column('raw_material', sa.String(length=9), nullable=True),
        sa.Column('raw_weight', sa.DECIMAL(), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('year'),
        sa.PrimaryKeyConstraint('plant'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('espec'),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_index(op.f('ix_material_espec_std_me_composite'), 'material_espec_std_me', ['year', 'plant', 'material', 'espec'])


def downgrade() -> None:
    op.drop_index(op.f('ix_material_espec_std_me_composite'), table_name='material_espec_std_me')
    op.drop_index(op.f('ix_material_espec_std_me_composite'), table_name='material_espec_std_me')
    