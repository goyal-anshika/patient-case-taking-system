import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.security import get_current_user
from ..database import get_db
from ..models.case import PatientCase
from ..models.patient import Patient
from ..models.user import User
from ..schemas.case import (
    CaseCreate,
    CaseResponse,
    CaseUpdate,
)


router = APIRouter(
    prefix="/api/cases",
    tags=["Cases"],
)


@router.post(
    "",
    response_model=CaseResponse,
)
def create_case(
    data: CaseCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    patient = db.get(Patient, data.patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    case = PatientCase(
        patient_id=data.patient_id,
        status="draft",
    )

    db.add(case)
    db.commit()
    db.refresh(case)

    return case


@router.get(
    "/{case_id}",
    response_model=CaseResponse,
)
def get_case(
    case_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    case = db.get(PatientCase, case_id)

    if not case:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    return case


@router.put(
    "/{case_id}",
    response_model=CaseResponse,
)
def update_case(
    case_id: uuid.UUID,
    data: CaseUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    case = db.get(PatientCase, case_id)

    if not case:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    updates = data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(case, key, value)

    db.commit()
    db.refresh(case)

    return case


@router.get(
    "/patient/{patient_id}",
    response_model=list[CaseResponse],
)
def get_patient_cases(
    patient_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    return (
        db.query(PatientCase)
        .filter(PatientCase.patient_id == patient_id)
        .order_by(PatientCase.created_at.desc())
        .all()
    )