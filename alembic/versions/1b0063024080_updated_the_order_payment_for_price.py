"""updated the order payment for price

Revision ID: 1b0063024080
Revises: e12bc9d0488f
Create Date: 2024-08-05 22:32:58.179261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b0063024080'
down_revision: Union[str, None] = 'e12bc9d0488f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Orders', sa.Column('price_per_item', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Orders', 'price_per_item')
    # ### end Alembic commands ###
