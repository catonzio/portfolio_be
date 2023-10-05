"""email_remove_nullable

Revision ID: 183dc1bdfee3
Revises: b399f6bf55ea
Create Date: 2023-10-05 22:22:23.315590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '183dc1bdfee3'
down_revision: Union[str, None] = 'b399f6bf55ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('emails', 'sender_name', nullable=False)


def downgrade() -> None:
    op.alter_column('emails', 'sender_name', nullable=True)
