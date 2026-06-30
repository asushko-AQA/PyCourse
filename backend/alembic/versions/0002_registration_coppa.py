"""registration: COPPA fields on users + single-use verification tokens

Revision ID: 0002_registration_coppa
Revises: 0001_initial_schema
Create Date: 2026-06-30
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa

revision: str = "0002_registration_coppa"
down_revision: str | None = "0001_initial_schema"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("is_minor", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.add_column("users", sa.Column("guardian_email", sa.String(), nullable=True))
    op.add_column(
        "users",
        sa.Column(
            "parental_consent",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )
    op.add_column(
        "users",
        sa.Column("parental_consent_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.add_column(
        "email_verification_tokens",
        sa.Column("consumed_at", sa.DateTime(timezone=True), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("email_verification_tokens", "consumed_at")
    op.drop_column("users", "parental_consent_at")
    op.drop_column("users", "parental_consent")
    op.drop_column("users", "guardian_email")
    op.drop_column("users", "is_minor")
