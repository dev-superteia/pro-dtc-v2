"""material_espec_zp58

Revision ID: 2834de88a8bd
Revises: 8ccaaea68ffe
Create Date: 2023-01-06 16:47:31.844856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2834de88a8bd'
down_revision = '8ccaaea68ffe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'material_espec_zp58',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=4), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('tt_weight', sa.DECIMAL(), nullable=False),
        sa.Column('mp_weight', sa.DECIMAL(), nullable=False),
        sa.Column('me_weight', sa.DECIMAL(), nullable=False),
        sa.Column('componente', sa.String(length=9), nullable=False),
        sa.Column('thickness', sa.Integer(), nullable=False),
        sa.Column('mat_me', sa.String(length=9), nullable=False),
        sa.Column('fol_inf_thick', sa.DECIMAL(), nullable=True),
        sa.Column('fol_sup_thick', sa.DECIMAL(), nullable=True),
        sa.Column('text_weight', sa.DECIMAL(), nullable=False),
        sa.Column('mat_me_weight', sa.DECIMAL(), nullable=False),
        sa.Column('text_thick', sa.Integer(), nullable=False),
        sa.Column('total_weight', sa.DECIMAL(), nullable=False),
        sa.Column('distinct_wire', sa.String(length=30), nullable=True),
        sa.Column('status', sa.String(length=4), nullable=False),
        sa.Column('emb_speed', sa.Integer(), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('plant'),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('componente'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_material_espec_zp58_composite'), 'material_espec_zp58', ['plant', 'material', 'componente'])


def downgrade() -> None:
    op.drop_index(op.f('ix_material_espec_zp58_composite'), table_name='material_espec_zp58')
    op.drop_table('material_espec_zp58')
    