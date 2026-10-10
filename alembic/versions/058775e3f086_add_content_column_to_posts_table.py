"""add content column to posts table

Revision ID: 058775e3f086
Revises: 4af8fa9b2f37
Create Date: 2026-04-09 18:51:07.177312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '058775e3f086'
down_revision: Union[str, Sequence[str], None] = '4af8fa9b2f37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    #"""Upgrade schema."""
    op.add_column('posts',sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade() -> None:
   # """Downgrade schema."""
   op.drop_column('posts', 'content')
   pass
