"""add few columns to posts table

Revision ID: 3a20872b291d
Revises: 76ca65b7a1ae
Create Date: 2026-04-10 14:12:43.184611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a20872b291d'
down_revision: Union[str, Sequence[str], None] = '76ca65b7a1ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    #"""Upgrade schema."""
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False, server_default='True'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                                    server_default=sa.text('now()'),nullable=False),)
    pass


def downgrade() -> None:
    #"""Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
