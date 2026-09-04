import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ConsultationCreate(BaseModel):
    patient_id: uuid.UUID
    case_id: uuid.UUID
    clinical_notes: str | None = None
    diagnosis: str | None = None
    prescription: str | None = None


class ConsultationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    patient_id: uuid.UUID
    case_id: uuid.UUID
    doctor_id: str
    clinical_notes: str | None
    diagnosis: str | None
    prescription: str | None
    created_at: datetime