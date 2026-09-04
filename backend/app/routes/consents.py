import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.security import get_current_user
from ..database import get_db
from ..models.consent import Consent
from ..models.patient import Patient
from ..models.user import User
from ..schemas.consent import (
    ConsentCreate,
    ConsentResponse,
)


router = APIRouter(
    prefix="/api/consents",
    tags=["Consent"],
)


@router.post(
    "",
    response_model=ConsentResponse,
)
def create_consent(
    data: ConsentCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    patient = db.get(Patient, data.patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    consent = Consent(
        **data.model_dump(),
        granted_at=(
            datetime.utcnow()
            if data.granted
            else None
        ),
    )

    db.add(consent)
    db.commit()
    db.refresh(consent)

    return consent


@router.get(
    "/patient/{patient_id}",
    response_model=list[ConsentResponse],
)
def get_patient_consents(
    patient_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    patient = db.get(Patient, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    return (
        db.query(Consent)
        .filter(Consent.patient_id == patient_id)
        .all()
    )


@router.post(
    "/{consent_id}/revoke",
    response_model=ConsentResponse,
)
def revoke_consent(
    consent_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    consent = db.get(Consent, consent_id)

    if not consent:
        raise HTTPException(
            status_code=404,
            detail="Consent not found",
        )

    consent.granted = False
    consent.revoked_at = datetime.utcnow()

    db.commit()
    db.refresh(consent)

    return consent