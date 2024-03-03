"""cors

Revision ID: b411032486bc
Revises: 0f81e0cdf499
Create Date: 2024-03-03 09:45:45.646225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b411032486bc'
down_revision: Union[str, None] = '0f81e0cdf499'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
