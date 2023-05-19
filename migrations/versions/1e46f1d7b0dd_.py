"""empty message

Revision ID: 1e46f1d7b0dd
Revises: 2affeda01447
Create Date: 2023-05-19 03:47:57.188780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e46f1d7b0dd'
down_revision = '2affeda01447'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rotation_period', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('orbital_period', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('diameter', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('climate', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('gravity', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('terrain', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('population', sa.Integer(), nullable=True))
        batch_op.drop_column('mass')
        batch_op.drop_column('homeworld')
        batch_op.drop_column('birth_year')
        batch_op.drop_column('height')
        batch_op.drop_column('hair_color')
        batch_op.drop_column('skin_color')
        batch_op.drop_column('gender')
        batch_op.drop_column('eye_color')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('eye_color', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('gender', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('skin_color', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('hair_color', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('height', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('birth_year', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('homeworld', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('mass', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_column('population')
        batch_op.drop_column('terrain')
        batch_op.drop_column('gravity')
        batch_op.drop_column('climate')
        batch_op.drop_column('diameter')
        batch_op.drop_column('orbital_period')
        batch_op.drop_column('rotation_period')

    # ### end Alembic commands ###
