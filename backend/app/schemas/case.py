import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CaseCreate(BaseModel):
    patient_id: uuid.UUID


class CaseUpdate(BaseModel):
    chief_complaint: str | None = None
    history_of_present_illness: str | None = None
    past_medical_history: str | None = None
    medications: str | None = None
    allergies: str | None = None
    ai_summary: str | None = None
    status: str | None = None


class CaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    patient_id: uuid.UUID
    chief_complaint: str | None
    history_of_present_illness: str | None
    past_medical_history: str | None
    medications: str | None
    allergies: str | None
    ai_summary: str | None
    status: str
    created_at: datetime
    updated_at: datetime