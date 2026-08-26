import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Invitation, Template
from app.schemas.invitation import InvitationCreate


class InvitationService:

    @staticmethod
    def create_invitation(
        session: Session,
        payload: InvitationCreate,
    ) -> Invitation:

        # 1. Verificar que la plantilla exista
        template = session.scalar(
            select(Template).where(
                Template.id == payload.template_id
            )
        )

        if template is None:
            raise ValueError("Template not found")

        # 2. Generar identificadores
        invitation_id = uuid.uuid4()
        url_slug = uuid.uuid4().hex[:16]

        # 3. Crear la invitación
        invitation = Invitation(
            id=invitation_id,
            url_slug=url_slug,
            template_id=payload.template_id,
            data=payload.data.model_dump(mode="json"),
            selected_variant=payload.selected_variant,
            status="DRAFT",
        )

        # 4. Guardar
        session.add(invitation)
        session.commit()
        session.refresh(invitation)

        return invitation