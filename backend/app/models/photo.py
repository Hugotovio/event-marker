import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Photo(Base):
    __tablename__ = "photos"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    invitation_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("invitations.id", ondelete="CASCADE"),
        nullable=False,
    )

    slot_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    s3_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    upload_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    invitation: Mapped["Invitation"] = relationship(
        "Invitation",
        back_populates="photos",
    )