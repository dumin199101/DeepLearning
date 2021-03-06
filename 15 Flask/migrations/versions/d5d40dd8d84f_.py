"""empty message

Revision ID: d5d40dd8d84f
Revises: 57c551623cc8
Create Date: 2019-12-19 15:09:07.186235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5d40dd8d84f'
down_revision = '57c551623cc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_user', sa.Column('city', sa.String(length=64), nullable=True))
    op.create_foreign_key(None, 'tb_user', 'tb_role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tb_user', type_='foreignkey')
    op.drop_column('tb_user', 'city')
    # ### end Alembic commands ###
