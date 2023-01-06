"""material_espec_std_tm_table

Revision ID: 140955525fe4
Revises: de0b75e1d9fe
Create Date: 2023-01-06 15:07:54.816817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '140955525fe4'
down_revision = 'de0b75e1d9fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_espec_std_tm',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=4), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('espec', sa.String(length=20), nullable=False),
        sa.Column('raw_material', sa.String(length=9), nullable=False),
        sa.Column('comp_material', sa.String(length=9), nullable=False),
        sa.Column('raw_weight', sa.DECIMAL(), nullable=False),
        sa.Column('comp_weight', sa.DECIMAL(), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('year'),
        sa.PrimaryKeyConstraint('plant'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('espec'),
        sa.PrimaryKeyConstraint('raw_material'),
        sa.PrimaryKeyConstraint('comp_material'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_material_espec_std_tm_composite'), 'material_espec_std_tm', ['year', 'plant', 'material', 'espec', 'raw_material', 'comp_material'])


def downgrade() -> None:
    op.drop_index(op.f('ix_material_espec_std_tm_composite'), table_name='material_espec_std_tm')
    op.drop_table('material_espec_std_tm')
    