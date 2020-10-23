"""v0.7.2

Revision ID: aa8c3bf3c8d2
Revises: e63976281064
Create Date: 2020-10-23 17:56:01.253871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa8c3bf3c8d2'
down_revision = 'e63976281064'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment_history', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('payment_history', sa.Column('sum', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payment_history', 'sum')
    op.drop_column('payment_history', 'date')
    # ### end Alembic commands ###