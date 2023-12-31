"""Traer cambios de github

Revision ID: cac9b1747bc4
Revises: 4b9e15b1446f
Create Date: 2023-08-02 19:10:06.755859

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cac9b1747bc4'
down_revision = '4b9e15b1446f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('categoria_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'categoria', ['categoria_id'], ['id'])

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clave', sa.String(length=100), nullable=False))
        batch_op.drop_column('contraseña')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contraseña', mysql.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('clave')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('categoria_id')

    # ### end Alembic commands ###
