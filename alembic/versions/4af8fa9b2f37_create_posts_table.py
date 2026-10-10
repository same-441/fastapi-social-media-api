"""create posts table

Revision ID: 4af8fa9b2f37
Revises: 
Create Date: 2026-04-09 17:05:24.898789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4af8fa9b2f37'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    #"""Upgrade schema."""
     op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False , primary_key=True),
                     sa.Column('title',sa.String(),nullable=False))
     pass


def downgrade() -> None:
   # """Downgrade schema."""
   op.drop_table('posts')
   pass
