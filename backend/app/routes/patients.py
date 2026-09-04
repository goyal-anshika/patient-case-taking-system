import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.security import get_current_user
from ..database import get_db
from ..models.patient import Patient
from ..models.user import User
from ..schemas.patient import (
    PatientCreate,
    PatientResponse,
    PatientUpdate,
)


router = APIRouter(
    prefix="/api/patients",
    tags=["Patients"],
)


@router.post(
    "",
    response_model=PatientResponse,
)
def create_patient(
    data: PatientCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    existing = (
        db.query(Patient)
        .filter(
            Patient.patient_identifier
            == data.patient_identifier
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Patient identifier already exists",
        )

    patient = Patient(**data.model_dump())

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient


@router.get(
    "",
    response_model=list[PatientResponse],
)
def list_patients(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    return db.query(Patient).all()


@router.get(
    "/{patient_id}",
    response_model=PatientResponse,
)
def get_patient(
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

    return patient


@router.put(
    "/{patient_id}",
    response_model=PatientResponse,
)
def update_patient(
    patient_id: uuid.UUID,
    data: PatientUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    patient = db.get(Patient, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    updates = data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)

    return patient