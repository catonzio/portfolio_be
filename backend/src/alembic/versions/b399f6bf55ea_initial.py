"""initial

Revision ID: b399f6bf55ea
Revises: 
Create Date: 2023-10-05 22:16:52.890911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b399f6bf55ea'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename the 'sender' column to 'sender_email'
    op.alter_column('emails', 'sender', new_column_name='sender_email')

    # Add the 'sender_name' column
    op.add_column('emails', sa.Column('sender_name', sa.String(length=255), nullable=True))


def downgrade() -> None:
    # This is usually the reverse of the upgrade steps
    op.alter_column('emails', 'sender_email', new_column_name='sender')
    op.drop_column('emails', 'sender_name')
