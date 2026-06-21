"""Rename alias.subdomain to alias.path and expand length

Revision ID: a1b2c3d4e5f6
Revises: 31fe53421216
Create Date: 2026-06-20 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a1b2c3d4e5f6"
down_revision: Union[str, Sequence[str], None] = "4fe4c96ad3dd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "alias",
        "subdomain",
        new_column_name="path",
        type_=sa.String(255),
        existing_type=sa.String(63),
        existing_nullable=False,
    )
    op.drop_constraint("alias_subdomain_key", "alias", type_="unique")
    op.create_unique_constraint("alias_path_key", "alias", ["path"])


def downgrade() -> None:
    op.drop_constraint("alias_path_key", "alias", type_="unique")
    op.alter_column(
        "alias",
        "path",
        new_column_name="subdomain",
        type_=sa.String(63),
        existing_type=sa.String(255),
        existing_nullable=False,
    )
    op.create_unique_constraint("alias_subdomain_key", "alias", ["subdomain"])
