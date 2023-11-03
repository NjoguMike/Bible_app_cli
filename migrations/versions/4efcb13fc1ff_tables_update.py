"""Tables Update

Revision ID: 4efcb13fc1ff
Revises: dd2df52b04be
Create Date: 2023-11-03 17:13:04.495835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4efcb13fc1ff'
down_revision: Union[str, None] = 'dd2df52b04be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bibles', sa.Column('book', sa.String(), nullable=True))
    op.add_column('bibles', sa.Column('version', sa.String(), nullable=True))
    op.drop_column('bibles', 'bible_version')
    op.drop_column('bibles', 'bible_chapter')
    op.add_column('notes', sa.Column('bible_version', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notes', 'bible_version')
    op.add_column('bibles', sa.Column('bible_chapter', sa.VARCHAR(), nullable=True))
    op.add_column('bibles', sa.Column('bible_version', sa.VARCHAR(), nullable=True))
    op.drop_column('bibles', 'version')
    op.drop_column('bibles', 'book')
    # ### end Alembic commands ###