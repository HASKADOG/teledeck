"""v0.7.1

Revision ID: e63976281064
Revises: 94608a696ab0
Create Date: 2020-10-23 17:28:19.872517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e63976281064'
down_revision = '94608a696ab0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ads', sa.Column('bonus_used', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ads', 'bonus_used')
    # ### end Alembic commands ###
