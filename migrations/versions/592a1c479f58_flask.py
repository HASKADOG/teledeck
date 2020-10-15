"""flask

Revision ID: 592a1c479f58
Revises: 
Create Date: 2020-10-15 15:59:31.447823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '592a1c479f58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('promocodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('promocode', sa.String(length=32), nullable=True),
    sa.Column('date_start', sa.Date(), nullable=True),
    sa.Column('date_expires', sa.Date(), nullable=True),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('taken', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('second_name', sa.String(length=64), nullable=True),
    sa.Column('third_name', sa.String(length=64), nullable=True),
    sa.Column('is_entity', sa.Boolean(), nullable=True),
    sa.Column('entity_name', sa.String(length=64), nullable=True),
    sa.Column('iin', sa.Integer(), nullable=True),
    sa.Column('ogrn', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('phone_number', sa.BigInteger(), nullable=True),
    sa.Column('status', sa.String(length=8), nullable=True),
    sa.Column('ref_code', sa.String(length=16), nullable=True),
    sa.Column('ref_master_code', sa.String(length=16), nullable=True),
    sa.Column('register_date', sa.DateTime(), nullable=True),
    sa.Column('referrals', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('ref_code')
    )
    op.create_table('variables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track', sa.String(length=64), nullable=True),
    sa.Column('notify_email', sa.String(length=128), nullable=True),
    sa.Column('is_entity', sa.Boolean(), nullable=True),
    sa.Column('entity_name', sa.String(length=64), nullable=True),
    sa.Column('iin', sa.Integer(), nullable=True),
    sa.Column('ogrn', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('second_name', sa.String(length=64), nullable=True),
    sa.Column('third_name', sa.String(length=64), nullable=True),
    sa.Column('individual_phone_number', sa.Integer(), nullable=True),
    sa.Column('promocode', sa.String(length=16), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('ad_type', sa.String(length=20), nullable=True),
    sa.Column('is_custom', sa.Boolean(), nullable=True),
    sa.Column('template_data', sa.String(length=512), nullable=True),
    sa.Column('img_path', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=64), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('apply_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('new', sa.Boolean(), nullable=True),
    sa.Column('edited', sa.Boolean(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('debug', sa.String(length=22), nullable=True),
    sa.Column('time', sa.String(length=512), nullable=True),
    sa.Column('ref_discount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('track')
    )
    op.create_table('ads_updates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ad_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=64), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['ad_id'], ['ads.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ads_updates')
    op.drop_table('ads')
    op.drop_table('variables')
    op.drop_table('users')
    op.drop_table('time')
    op.drop_table('promocodes')
    # ### end Alembic commands ###
