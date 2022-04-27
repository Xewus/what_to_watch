"""added added_by field

Revision ID: b7b59e8085df
Revises: 
Create Date: 2022-04-27 16:02:35.119374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7b59e8085df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('opinion', sa.Column('added_by', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('opinion', 'added_by')
    # ### end Alembic commands ###