import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.security import get_current_user
from ..database import get_db
from ..models.case import PatientCase
from ..models.case_response import CaseResponse
from ..models.user import User
from ..schemas.case_response import (
    CaseResponseCreate,
    CaseResponseRead,
)


router = APIRouter(
    prefix="/api/case-responses",
    tags=["Case Responses"],
)


@router.post(
    "",
    response_model=CaseResponseRead,
)
def add_case_response(
    data: CaseResponseCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    case = db.get(PatientCase, data.case_id)

    if not case:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    response = CaseResponse(
        **data.model_dump()
    )

    db.add(response)
    db.commit()
    db.refresh(response)

    return response


@router.get(
    "/case/{case_id}",
    response_model=list[CaseResponseRead],
)
def get_case_responses(
    case_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    case = db.get(PatientCase, case_id)

    if not case:
        raise HTTPException(
            status_code=404,
            detail="Case not found",
        )

    return (
        db.query(CaseResponse)
        .filter(CaseResponse.case_id == case_id)
        .order_by(CaseResponse.created_at)
        .all()
    )