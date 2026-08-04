"""add user role"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "eca86b62c787"
down_revision: Union[str, Sequence[str], None] = "f20cc4b6d8d6"
branch_labels = None
depends_on = None


role_enum = postgresql.ENUM(
    "ADMIN",
    "USER",
    name="role",
)


def upgrade():
    role_enum.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "user",
        sa.Column(
            "role",
            role_enum,
            nullable=False,
            server_default="USER",
        ),
    )

    op.alter_column(
        "user",
        "role",
        server_default=None,
    )


def downgrade():
    op.drop_column("user", "role")

    role_enum.drop(
        op.get_bind(),
        checkfirst=True,
    )