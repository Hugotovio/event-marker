import sys
import uuid

from sqlalchemy import select

sys.path.insert(0, "backend")

from app.db.database import SessionLocal
from app.models import Invitation, Template
from app.schemas.invitation import InvitationCreate
from app.services.invitation_service import InvitationService


def test_create_invitation_service():
    session = SessionLocal()

    template = None
    invitation = None

    try:
        # Crear template de prueba
        template = Template(
            id=uuid.uuid4(),
            name=f"Service Test {uuid.uuid4().hex[:8]}",
            description="Template para prueba del servicio",
            version="1.0.0",
            is_active=True,
        )

        session.add(template)
        session.commit()
        session.refresh(template)

        # Datos de entrada
        payload = InvitationCreate(
            template_id=template.id,
            selected_variant="classic",
            data={
                "event": {
                    "name": "Evento de prueba",
                    "date": "2026-12-20",
                    "time": "19:00:00",
                    "timezone": "America/Bogota",
                    "location": "Cartagena",
                }
            },
        )

        # Ejecutar servicio
        invitation = InvitationService.create_invitation(
            session=session,
            payload=payload,
        )

        # Comprobaciones
        assert invitation is not None
        assert invitation.template_id == template.id
        assert invitation.selected_variant == "classic"
        assert invitation.status == "DRAFT"
        assert len(invitation.url_slug) == 16

        # Comprobar que realmente quedó en PostgreSQL
        result = session.scalar(
            select(Invitation).where(
                Invitation.id == invitation.id
            )
        )

        assert result is not None
        assert result.id == invitation.id

    finally:
        if invitation is not None:
            session.delete(invitation)

        if template is not None:
            session.delete(template)

        session.commit()
        session.close()