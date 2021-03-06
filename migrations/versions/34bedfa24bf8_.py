"""empty message

Revision ID: 34bedfa24bf8
Revises: a99410dd19b7
Create Date: 2017-02-26 16:05:22.498000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34bedfa24bf8'
down_revision = 'a99410dd19b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=64), nullable=True),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.Column('pub_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_photos_pub_time'), 'photos', ['pub_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_photos_pub_time'), table_name='photos')
    op.drop_table('photos')
    # ### end Alembic commands ###
