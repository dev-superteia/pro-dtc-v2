"""create md_material table

Revision ID: d8ee6def7230
Revises: 13532e87ef69
Create Date: 2023-01-05 20:46:28.519919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8ee6def7230'
down_revision = '13532e87ef69'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'md_material',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('material', sa.String(length=9), nullable=False),
        sa.Column('mat_desc', sa.String(length=70), nullable=False),
        sa.Column('subclass', sa.String(length=50), nullable=True),
        sa.Column('family', sa.String(length=50), nullable=True),
        sa.Column('mkg_segm', sa.String(length=4), nullable=True),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('material'),
        sa.PrimaryKeyConstraint('mat_desc'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_md_material_composite'), 'md_material', ['material', 'mat_desc'])


def downgrade():
    op.drop_index(op.f('ix_md_material_composite'), table_name='md_material')
    op.drop_table('md_material')
