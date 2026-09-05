from pydantic import BaseModel, Field


class ClinicalExtraction(BaseModel):

    chief_complaint: str | None = None
    onset: str | None = None
    duration: str | None = None
    location: str | None = None
    severity: str | None = None
    character: str | None = None
    aggravating_factors: str | None = None
    relieving_factors: str | None = None
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