"""change column name to title in Producs table

Revision ID: c184d6724430
Revises: 65127098d704
Create Date: 2024-01-05 08:24:08.735736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c184d6724430'
down_revision: Union[str, None] = '65127098d704'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
