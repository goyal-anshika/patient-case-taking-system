from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.ai.summarization.case_summary import (
    generate_case_summary,
)


router = APIRouter(
    prefix="/api/ai",
    tags=["AI - Pipeline"],
)


class PipelineRequest(BaseModel):

    responses: list[dict] = Field(
        default_factory=list
    )

    ocr_text: str | None = None


@router.post("/case-summary")
async def case_summary(
    request: PipelineRequest,
):

    summary = await generate_case_summary(
        responses=request.responses,
        ocr_text=request.ocr_text,
    )

    return {
        "summary": summary,
        "review_required": True,
        "source_count": (
            len(request.responses)
            + (1 if request.ocr_text else 0)
        ),
    }