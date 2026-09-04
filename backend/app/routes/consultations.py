import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.security import get_current_user
from ..database import get_db
from ..models.case import PatientCase
from ..models.consultation import Consultation
from ..models.patient import Patient
from ..models.user import User
from ..schemas.consultation import (
    ConsultationCreate,
    ConsultationResponse,
)


router = APIRouter(
    prefix="/api/consultations",
    tags=["Consultations"],
)


@router.post(
    "",
    response_model=ConsultationResponse,
)
def create_consultation(
    data: ConsultationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    patient = db.get(Patient, data.patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    case = db.get(PatientCase, data.case_id)

    if not case:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    consultation = Consultation(
        patient_id=data.patient_id,
        case_id=data.case_id,
        doctor_id=str(current_user.id),
        clinical_notes=data.clinical_notes,
        diagnosis=data.diagnosis,
        prescription=data.prescription,
    )

    db.add(consultation)

    case.status = "completed"

    db.commit()
    db.refresh(consultation)

    return consultation


@router.get(
    "/{consultation_id}",
    response_model=ConsultationResponse,
)
def get_consultation(
    consultation_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    consultation = db.get(
        Consultation,
        consultation_id,
    )

    if not consultation:
        raise HTTPException(
            status_code=404,
            detail="Consultation not found",
        )

    return consultation


@router.get(
    "/patient/{patient_id}",
    response_model=list[ConsultationResponse],
)
def get_patient_consultations(
    patient_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    return (
        db.query(Consultation)
        .filter(
            Consultation.patient_id
            == patient_id
        )
        .order_by(
            Consultation.created_at.desc()
        )
        .all()
    )