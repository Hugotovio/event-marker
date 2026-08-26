import sys
import uuid

from sqlalchemy import select

sys.path.insert(0, "backend")

from app.db.database import SessionLocal
from app.models import Invitation, Photo, Template, TemplateVariant


def test_template_invitation_photo_flow():
    session = SessionLocal()

    template = None
    variant = None
    invitation = None
    photo = None

    try:
        # 1. Crear plantilla
        template = Template(
            id=uuid.uuid4(),
            name=f"Test Template {uuid.uuid4().hex[:8]}",
            description="Plantilla para prueba de integración",
            version="1.0.0",
            is_active=True,
        )

        session.add(template)
        session.flush()

        # 2. Crear variante asociada a la plantilla
        variant = TemplateVariant(
            id=uuid.uuid4(),
            template_id=template.id,
            name="classic",
            description="Variante clásica",
            css_path="templates/test/classic.css",
            is_active=True,
        )

        session.add(variant)
        session.flush()

        # 3. Crear invitación asociada a la plantilla
        invitation = Invitation(
            id=uuid.uuid4(),
            url_slug=uuid.uuid4().hex[:16],
            template_id=template.id,
            data={
                "event": {
                    "name": "Evento de prueba",
                    "date": "2026-12-12",
                    "time": "18:00",
                    "timezone": "America/Bogota",
                    "location": "Cartagena",
                }
            },
            selected_variant="classic",
            status="DRAFT",
        )

        session.add(invitation)
        session.flush()

        # 4. Crear fotografía asociada a la invitación
        photo = Photo(
            id=uuid.uuid4(),
            invitation_id=invitation.id,
            slot_name="hero",
            s3_path="test/invitations/photo.jpg",
        )

        session.add(photo)

        # 5. Confirmar todos los registros
        session.commit()

        # 6. Consultar nuevamente la invitación
        result = session.scalar(
            select(Invitation).where(
                Invitation.id == invitation.id
            )
        )

        assert result is not None
        assert result.template_id == template.id
        assert result.selected_variant == "classic"
        assert result.status == "DRAFT"

        # 7. Comprobar que la relación con Template funciona
        assert result.template is not None
        assert result.template.id == template.id

        # 8. Comprobar que la relación con Photo funciona
        assert len(result.photos) == 1
        assert result.photos[0].id == photo.id
        assert result.photos[0].slot_name == "hero"

        # 9. Comprobar que Template conoce sus relaciones
        assert len(template.variants) == 1
        assert template.variants[0].id == variant.id

        assert len(template.invitations) == 1
        assert template.invitations[0].id == invitation.id

    finally:
        # Eliminamos los datos creados por la prueba.
        if invitation is not None:
            session.delete(invitation)

        if variant is not None:
            session.delete(variant)

        if template is not None:
            session.delete(template)

        session.commit()
        session.close()