"""empty message

Revision ID: d14b950d682a
Revises: 71ab5af0f837
Create Date: 2024-07-31 21:36:36.744317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd14b950d682a'
down_revision = '71ab5af0f837'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###
