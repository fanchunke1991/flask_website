"""empty message

Revision ID: 00932cb7698c
Revises: 1b89f94dc7cd
Create Date: 2017-02-13 23:38:03.839000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '00932cb7698c'
down_revision = '1b89f94dc7cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'comments_ibfk_2', 'comments', type_='foreignkey')
    op.drop_column('comments', 'message_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('message_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key(u'comments_ibfk_2', 'comments', 'messages', ['message_id'], ['id'])
    # ### end Alembic commands ###