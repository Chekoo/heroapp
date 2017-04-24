"""markdown

Revision ID: 4281bae42585
Revises: e0decc9e6f99
Create Date: 2017-04-12 16:24:40.479516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4281bae42585'
down_revision = 'e0decc9e6f99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
