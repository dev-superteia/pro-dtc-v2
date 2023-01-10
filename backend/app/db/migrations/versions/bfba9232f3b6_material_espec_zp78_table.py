"""material_espec_zp78_table

Revision ID: bfba9232f3b6
Revises: 2834de88a8bd
Create Date: 2023-01-06 16:50:36.519945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfba9232f3b6'
down_revision = '2834de88a8bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_espec_zp78',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=4), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('tm_weight', sa.DECIMAL(), nullable=False),
        sa.Column('mp_weight', sa.DECIMAL(), nullable=False),
        sa.Column('me_weight', sa.DECIMAL(), nullable=False),
        sa.Column('mat_mp', sa.String(length=9), nullable=False),
        sa.Column('thickness', sa.Integer(), nullable=False),
        sa.Column('mat_me', sa.String(length=9), nullable=False),
        sa.Column('fol_inf_thick', sa.DECIMAL(), nullable=True),
        sa.Column('fol_sup_thick', sa.DECIMAL(), nullable=True),
        sa.Column('text_weight', sa.DECIMAL(), nullable=True),
        sa.Column('mat_me_weight', sa.DECIMAL(), nullable=False),
        sa.Column('text_thick', sa.Integer(), nullable=True),
        sa.Column('total_weight', sa.DECIMAL(), nullable=False),
        sa.Column('rope_thick', sa.DECIMAL(), nullable=True),
        sa.Column('rope_number', sa.Integer(), nullable=True),
        sa.Column('status', sa.String(length=4), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('plant'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('mat_mp'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_material_espec_zp78_composite'), 'material_espec_zp78', ['plant', 'material', 'mat_mp'])


def downgrade() -> None:
    op.drop_index(op.f('ix_material_espec_zp78_composite'), table_name='material_espec_zp78')
    op.drop_table('material_espec_zp78')
