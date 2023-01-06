"""market_segment_table

Revision ID: c6e06203b539
Revises: d8ee6def7230
Create Date: 2023-01-06 14:57:59.654054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6e06203b539'
down_revision = 'd8ee6def7230'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'market_segment',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('mkg_segm', sa.String(length=4), nullable=True),
        sa.Column('line', sa.String(length=40), nullable=False),
        sa.Column('bu', sa.String(length=10), nullable=True),
        sa.Column('denomination', sa.String(length=40), nullable=True),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('market_segment')
