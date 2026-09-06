from typing import Any
from pydantic import BaseModel, Field


class ClinicalAnswer(BaseModel):
    field: str
    value: Any
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    source: str = "conversation"


class ClinicalExtraction(BaseModel):
    chief_complaint: str | None = None

    onset: str | None = None
    duration: str | None = None
    location: str | None = None
    severity: str | None = None
    character: str | None = None

    aggravating_factors: list[str] = Field(
        default_factory=list
    )

    relieving_factors: list[str] = Field(
        default_factory=list
    )

    associated_symptoms: list[str] = Field(
        default_factory=list
    )

    past_medical_history: list[str] = Field(
        default_factory=list
    )

    medications: list[str] = Field(
        default_factory=list
    )

    allergies: list[str] = Field(
        default_factory=list
    )