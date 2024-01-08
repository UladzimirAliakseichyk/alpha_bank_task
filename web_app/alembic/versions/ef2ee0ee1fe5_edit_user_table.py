"""edit user table

Revision ID: ef2ee0ee1fe5
Revises: 520b1810db5a
Create Date: 2024-01-08 10:04:16.455968

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef2ee0ee1fe5'
down_revision: Union[str, None] = '520b1810db5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_password', sa.String(), nullable=True))
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_password', table_name='user')
    op.create_index(op.f('ix_user_hashed_password'), 'user', ['hashed_password'], unique=False)
    op.drop_column('user', 'password')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_hashed_password'), table_name='user')
    op.create_index('ix_user_password', 'user', ['password'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.drop_column('user', 'hashed_password')
    # ### end Alembic commands ###