"""2302_ending_14

Revision ID: 453e47e43543
Revises: 0f2822f483b2
Create Date: 2024-02-23 17:32:54.034862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '453e47e43543'
down_revision: Union[str, None] = '0f2822f483b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image_tag_association', sa.Column('comment_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'image_tag_association', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'image_tag_association', type_='foreignkey')
    op.drop_column('image_tag_association', 'comment_id')
    # ### end Alembic commands ###
