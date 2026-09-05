import uuid

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.ai.summarization.case_summary import (
    generate_case_summary,
)
from app.core.security import (
    get_current_user,
)
from app.database import get_db
from app.models.case import PatientCase
from app.models.case_response import CaseResponse
from app.models.document import Document
from app.models.user import User


router = APIRouter(
    prefix="/api/ai/cases",
    tags=["AI - Case"],
)


@router.post("/{case_id}/summarize")
async def summarize_existing_case(
    case_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    case = db.get(
        PatientCase,
        case_id,
    )

    if not case:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    responses = (
        db.query(CaseResponse)
        .filter(
            CaseResponse.case_id == case_id
        )
        .all()
    )

    documents = (
        db.query(Document)
        .filter(
            Document.patient_id
            == case.patient_id
        )
        .all()
    )

    response_data = [
        {
            "question": item.question,
            "answer": item.answer,
            "source": item.source,
        }
        for item in responses
    ]

    document_text = "\n".join(
        doc.extracted_text or ""
        for doc in documents
    )

    summary = await generate_case_summary(
        responses=response_data,
        ocr_text=document_text,
    )

    case.ai_summary = str(summary)

    db.commit()
    db.refresh(case)

    return {
        "case_id": str(case.id),
        "summary": summary,
        "review_required": True,
    }