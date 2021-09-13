"""empty message

Revision ID: 40557a55e174
Revises: 0f9ddf8fec06
Create Date: 2021-09-13 03:11:26.003799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40557a55e174'
down_revision = '0f9ddf8fec06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'product_user', ['user_id', 'product_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product_user', type_='unique')
    # ### end Alembic commands ###