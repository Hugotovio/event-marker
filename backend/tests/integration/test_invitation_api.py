import sys
import uuid

from fastapi.testclient import TestClient
from sqlalchemy import select

sys.path.insert(0, "backend")

from app.db.database import SessionLocal
from app.main import app
from app.models import Invitation, Template


client = TestClient(app)


def test_create_invitation_api():
    session = SessionLocal()

    template = Template(
        id=uuid.uuid4(),
        name=f"API Test Template {uuid.uuid4().hex[:8]}",
        description="Template para prueba de API",
        version="1.0.0",
        is_active=True,
    )

    session.add(template)
    session.commit()
    session.refresh(template)

    template_id = template.id

    session.close()

    payload = {
        "template_id": str(template_id),
        "selected_variant": "classic",
        "data": {
            "event": {
                "name": "Evento API Test",
                "date": "2026-12-20",
                "time": "19:00:00",
                "timezone": "America/Bogota",
                "location": "Cartagena",
                "address": "Centro Histórico",
            }
        },
    }

    response = client.post(
        "/api/v1/invitations",
        json=payload,
    )

    assert response.status_code == 201

    body = response.json()

    assert body["template_id"] == str(template_id)
    assert body["selected_variant"] == "classic"
    assert body["status"] == "DRAFT"
    assert body["data"]["event"]["name"] == "Evento API Test"

    invitation_id = body["id"]

    session = SessionLocal()

    try:
        invitation = session.scalar(
            select(Invitation).where(
                Invitation.id == uuid.UUID(invitation_id)
            )
        )

        assert invitation is not None
        assert invitation.template_id == template_id
        assert invitation.status == "DRAFT"

    finally:
        if invitation is not None:
            session.delete(invitation)

        template_db = session.scalar(
            select(Template).where(
                Template.id == template_id
            )
        )

        if template_db is not None:
            session.delete(template_db)

        session.commit()
        session.close()