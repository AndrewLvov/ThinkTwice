"""empty message

Revision ID: 9383b46d4c96
Revises: None
Create Date: 2016-10-08 17:22:24.084608

"""

# revision identifiers, used by Alembic.
revision = '9383b46d4c96'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('url')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site')
    ### end Alembic commands ###
