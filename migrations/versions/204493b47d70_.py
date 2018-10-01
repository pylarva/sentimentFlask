"""empty message

Revision ID: 204493b47d70
Revises: d9f37ccbf458
Create Date: 2018-09-30 00:22:41.458887

"""

# revision identifiers, used by Alembic.
revision = '204493b47d70'
down_revision = 'd9f37ccbf458'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Sentiment', sa.Column('customer', sa.String(length=80), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Sentiment', 'customer')
    ### end Alembic commands ###