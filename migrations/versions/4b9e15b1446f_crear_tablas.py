"""crear_tablas

Revision ID: 4b9e15b1446f
Revises: 27336de86ea7
Create Date: 2023-08-02 18:01:46.981735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b9e15b1446f'
down_revision = '27336de86ea7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('categoria_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'categoria', ['categoria_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('categoria_id')

    # ### end Alembic commands ###
