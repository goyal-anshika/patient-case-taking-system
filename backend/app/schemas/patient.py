import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PatientCreate(BaseModel):
    patient_identifier: str
    full_name: str
    date_of_birth: datetime | None = None
    gender: str | None = None
    phone_number: str | None = None
    abha_id: str | None = None


class PatientUpdate(BaseModel):
    full_name: str | None = None
    date_of_birth: datetime | None = None
    gender: str | None = None
    phone_number: str | None = None
    abha_id: str | None = None


class PatientResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    patient_identifier: str
    full_name: str
    date_of_birth: datetime | None
    gender: str | None
    phone_number: str | None
    abha_id: str | None
    is_active: bool
    created_at: datetime