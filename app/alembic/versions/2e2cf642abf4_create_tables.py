"""create tables

Revision ID: 2e2cf642abf4
Revises: cc1557bdd566
Create Date: 2024-09-02 21:51:11.190914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2e2cf642abf4'
down_revision: Union[str, None] = 'cc1557bdd566'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('names', sa.String(), nullable=False),
    sa.Column('count_interactions', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('first_interaction', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_interaction', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('amount_revenue', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('amount_payday', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('comissiontrading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expertise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('newtrading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scraptrading',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('is_user', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.Column('is_admin', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('is_super_admin', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_user', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False),
    sa.Column('is_admin', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('is_super_admin', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    sa.UniqueConstraint('phone_number', name='users_phone_number_key')
    )
    op.drop_table('user')
    op.drop_table('scraptrading')
    op.drop_table('newtrading')
    op.drop_table('expertise')
    op.drop_table('comissiontrading')
    op.drop_table('clients')
    # ### end Alembic commands ###
