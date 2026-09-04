import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CaseResponseCreate(BaseModel):
    case_id: uuid.UUID
    question: str
    answer: str
    source: str = "patient"


class CaseResponseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    case_id: uuid.UUID
    question: str
    answer: str
    source: str
    created_at: datetime