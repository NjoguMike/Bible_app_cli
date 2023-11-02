"""Data Relationship update

Revision ID: 7a1ba0d73c4a
Revises: dd2df52b04be
Create Date: 2023-11-02 16:31:56.322242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a1ba0d73c4a'
down_revision: Union[str, None] = 'dd2df52b04be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
