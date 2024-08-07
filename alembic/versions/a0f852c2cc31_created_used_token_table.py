"""created used token table

Revision ID: a0f852c2cc31
Revises: d458c70c73bc
Create Date: 2024-07-29 20:09:20.987089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0f852c2cc31'
down_revision: Union[str, None] = 'd458c70c73bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('used_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('used_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_used_tokens_id'), 'used_tokens', ['id'], unique=False)
    op.create_index(op.f('ix_used_tokens_token'), 'used_tokens', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_used_tokens_token'), table_name='used_tokens')
    op.drop_index(op.f('ix_used_tokens_id'), table_name='used_tokens')
    op.drop_table('used_tokens')
    # ### end Alembic commands ###
