"""create md_plant table

Revision ID: 13532e87ef69
Revises: 6d5ebb85f6c1
Create Date: 2023-01-05 20:45:26.167894

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '13532e87ef69'
down_revision = '6d5ebb85f6c1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'md_plant',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('plant', sa.String(length=40), nullable=False),
        sa.Column('plant_desc', sa.String(length=20), nullable=True),
        sa.Column('created_on', sa.TIMESTAMP(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
        op.drop_table('md_plant')
