from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.invitation import InvitationCreate, InvitationResponse
from app.services.invitation_service import InvitationService


router = APIRouter(
    prefix="/invitations",
    tags=["Invitations"],
)


@router.post(
    "",
    response_model=InvitationResponse,
    status_code=201,
)
def create_invitation(
    payload: InvitationCreate,
    db: Session = Depends(get_db),
):
    try:
        return InvitationService.create_invitation(
            session=db,
            payload=payload,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc