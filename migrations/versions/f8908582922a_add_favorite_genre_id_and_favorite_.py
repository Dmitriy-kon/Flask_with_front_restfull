"""add favorite_genre_id and favorite_genre relationship

Revision ID: f8908582922a
Revises: b46c486e9f35
Create Date: 2023-04-12 10:30:45.693094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8908582922a'
down_revision = 'b46c486e9f35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_genre_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_user_genre', 'genres', ['favorite_genre_id'], ['id'])
        batch_op.drop_column('favorite_genre')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_genre', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint('fk_user_genre', type_='foreignkey')
        batch_op.drop_column('favorite_genre_id')

    # ### end Alembic commands ###