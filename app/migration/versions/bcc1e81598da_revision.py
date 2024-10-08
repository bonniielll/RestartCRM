"""revision

Revision ID: bcc1e81598da
Revises: b5e0be9b64ac
Create Date: 2024-09-15 16:25:31.275036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bcc1e81598da'
down_revision: Union[str, None] = 'b5e0be9b64ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dailycash',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('magazine', sa.String(), nullable=False),
    sa.Column('manager', sa.String(), nullable=False),
    sa.Column('cash', sa.Float(), nullable=False),
    sa.Column('daytime', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dailycash')
    # ### end Alembic commands ###
