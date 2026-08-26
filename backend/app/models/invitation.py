import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Invitation(Base):
    __tablename__ = "invitations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    url_slug: Mapped[str] = mapped_column(
        String(16),
        unique=True,
        nullable=False,
    )

    template_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("templates.id", ondelete="RESTRICT"),
        nullable=False,
    )

    data: Mapped[dict[str, Any]] = mapped_column(
        JSONB,
        nullable=False,
    )

    selected_variant: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    published_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    template: Mapped["Template"] = relationship(
        "Template",
        back_populates="invitations",
    )

    photos: Mapped[list["Photo"]] = relationship(
        "Photo",
        back_populates="invitation",
        cascade="all, delete-orphan",
    )