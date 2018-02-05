"""empty message

Revision ID: 55d515270956
Revises: 2b0f24ff3140
Create Date: 2018-02-01 21:34:11.257785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55d515270956'
down_revision = '2b0f24ff3140'
branch_labels = None
depends_on = None


def upgrade():

   connection = op.get_bind()
   connection.execute("""

    INSERT INTO products (name) VALUES ('Stephen');

    """)

def downgrade():
    pass
