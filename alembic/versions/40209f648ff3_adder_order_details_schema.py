"""adder order details schema

Revision ID: 40209f648ff3
Revises: 1bcbfcd47518
Create Date: 2024-08-06 12:39:36.502236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40209f648ff3'
down_revision: Union[str, None] = '1bcbfcd47518'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Payment', sa.Column('product_code', sa.String(), nullable=False))
    op.add_column('Payment', sa.Column('ref_id', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Payment', 'ref_id')
    op.drop_column('Payment', 'product_code')
    # ### end Alembic commands ###
