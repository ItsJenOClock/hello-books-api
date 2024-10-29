"""attempting to remove author and isbn

Revision ID: 6c45ad4e46a4
Revises: 426471329e1a
Create Date: 2024-10-29 02:28:58.247142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c45ad4e46a4'
down_revision = '426471329e1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('author')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
