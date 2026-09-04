import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ConsentCreate(BaseModel):
    patient_id: uuid.UUID
    consent_type: str
    granted: bool
    consent_text: str | None = None


class ConsentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    patient_id: uuid.UUID
    consent_type: str
    granted: bool
    consent_text: str | None
    granted_at: datetime | None
    revoked_at: datetime | None
    created_at: datetime