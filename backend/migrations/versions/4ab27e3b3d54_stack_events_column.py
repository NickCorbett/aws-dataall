"""stack events column

Revision ID: 4ab27e3b3d54
Revises: 46e5a33450b1
Create Date: 2021-07-13 06:56:48.350712

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "4ab27e3b3d54"
down_revision = "46e5a33450b1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "stack",
        sa.Column("events", postgresql.JSON(astext_type=sa.Text()), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("stack", "events")
    # ### end Alembic commands ###
