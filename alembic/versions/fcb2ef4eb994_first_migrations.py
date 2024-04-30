"""first migrations

Revision ID: fcb2ef4eb994
Revises: 
Create Date: 2024-04-28 17:42:56.063916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcb2ef4eb994'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('email', sa.String(length=225), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=False),
    sa.Column('full_name', sa.String(length=225), nullable=False),
    sa.Column('is_active_true', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
