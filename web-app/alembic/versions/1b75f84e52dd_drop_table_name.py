"""drop_table_name

Revision ID: 1b75f84e52dd
Revises: ca94f7bb5f5c
Create Date: 2024-01-05 10:16:07.780383

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b75f84e52dd'
down_revision: Union[str, None] = 'ca94f7bb5f5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
