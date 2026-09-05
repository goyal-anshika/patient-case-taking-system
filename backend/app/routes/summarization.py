from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.ai.summarization.case_summary import (
    generate_case_summary,
)


router = APIRouter(
    prefix="/api/ai",
    tags=["AI - Summarisation"],
)


class SummaryRequest(BaseModel):

    responses: list[dict] = Field(
        default_factory=list
    )

    ocr_text: str | None = None


@router.post("/summarize")
async def summarize_case(
    request: SummaryRequest,
):

    summary = await generate_case_summary(
        responses=request.responses,
        ocr_text=request.ocr_text,
    )

    return {
        "summary": summary,
        "review_required": True,
    }