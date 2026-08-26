from datetime import date, time
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class EventData(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    date: date
    time: time
    timezone: str = Field(min_length=1, max_length=50)
    location: str = Field(min_length=1, max_length=200)
    address: str | None = Field(default=None, max_length=300)


class InvitationData(BaseModel):
    event: EventData


class InvitationCreate(BaseModel):
    template_id: UUID
    selected_variant: str = Field(min_length=1, max_length=100)
    data: InvitationData


class InvitationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    url_slug: str
    template_id: UUID
    selected_variant: str
    status: str
    data: dict[str, Any]