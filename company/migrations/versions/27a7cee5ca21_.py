"""empty message

Revision ID: 27a7cee5ca21
Revises: c2fe3333b44d
Create Date: 2018-03-27 18:33:43.773602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27a7cee5ca21'
down_revision = 'c2fe3333b44d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('click', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'click')
    # ### end Alembic commands ###
