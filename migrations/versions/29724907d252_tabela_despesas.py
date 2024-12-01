"""tabela despesas

Revision ID: 29724907d252
Revises: db3fa884894d
Create Date: 2024-12-01 12:33:12.843251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29724907d252'
down_revision: Union[str, None] = 'db3fa884894d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('despesas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('tipo', sa.String(), nullable=False),
    sa.Column('data_vencimento', sa.DateTime(), nullable=False),
    sa.Column('data_pagamento', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('despesas')
    # ### end Alembic commands ###
