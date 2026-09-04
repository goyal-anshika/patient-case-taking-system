import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from ..core.security import get_current_user
from ..database import get_db
from ..models.document import Document
from ..models.patient import Patient
from ..models.user import User


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"],
)


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_TYPES = {
    "image/jpeg",
    "image/png",
    "application/pdf",
}


@router.post("")
async def upload_document(
    patient_id: uuid.UUID = Form(...),
    document_type: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    patient = db.get(Patient, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type",
        )

    document_id = uuid.uuid4()

    extension = Path(
        file.filename or ""
    ).suffix.lower()

    stored_filename = (
        f"{document_id}{extension}"
    )

    destination = UPLOAD_DIR / stored_filename

    contents = await file.read()

    # Basic demo upload limit: 10 MB
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="File exceeds 10 MB limit",
        )

    destination.write_bytes(contents)

    document = Document(
        id=document_id,
        patient_id=patient_id,
        document_type=document_type,
        file_name=file.filename or stored_filename,
        file_path=str(destination),
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "id": str(document.id),
        "patient_id": str(document.patient_id),
        "document_type": document.document_type,
        "file_name": document.file_name,
        "message": "Document uploaded successfully",
    }


@router.get(
    "/patient/{patient_id}"
)
def get_patient_documents(
    patient_id: uuid.UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):

    patient = db.get(Patient, patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found",
        )

    documents = (
        db.query(Document)
        .filter(Document.patient_id == patient_id)
        .order_by(Document.created_at.desc())
        .all()
    )

    return documents