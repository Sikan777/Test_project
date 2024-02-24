"""2402_ending_02

Revision ID: 545f9fa76dc4
Revises: db08407b0b6b
Create Date: 2024-02-24 10:15:09.076364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '545f9fa76dc4'
down_revision: Union[str, None] = 'db08407b0b6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('picture_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'picture_count')
    # ### end Alembic commands ###
