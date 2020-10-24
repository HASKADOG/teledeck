"""v0.9.1

Revision ID: 5601a925440d
Revises: cfcd34a4490c
Create Date: 2020-10-23 23:55:41.692474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5601a925440d'
down_revision = 'cfcd34a4490c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restore_tokens', sa.Column('wasted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restore_tokens', 'wasted')
    # ### end Alembic commands ###
