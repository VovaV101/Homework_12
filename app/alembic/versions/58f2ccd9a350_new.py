"""new

Revision ID: 58f2ccd9a350
Revises: b411032486bc
Create Date: 2024-03-03 11:58:04.060820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58f2ccd9a350'
down_revision: Union[str, None] = 'b411032486bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
