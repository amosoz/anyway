"""add new table

Revision ID: 35b556aef8ef
Revises: 423a7ea74c0a
Create Date: 2018-12-10 11:31:29.518909

"""

# revision identifiers, used by Alembic.
revision = '35b556aef8ef'
down_revision = '423a7ea74c0a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_flash',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('accident', sa.Boolean(), nullable=True),
    sa.Column('author', sa.Text(), nullable=True),
    sa.Column('date', sa.TIMESTAMP(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('source', sa.Text(), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_flash')
    ### end Alembic commands ###
