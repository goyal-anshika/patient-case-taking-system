import tempfile

from fastapi import APIRouter, File, UploadFile

from app.ai.ocr.ocr_service import extract_text


router = APIRouter(
    prefix="/api/ai/ocr",
    tags=["AI - OCR"],
)


@router.post("/extract")
async def extract_document_text(
    file: UploadFile = File(...),
):

    contents = await file.read()

    suffix = ".png"

    if file.filename:
        suffix = (
            "." +
            file.filename.split(".")[-1]
        )

    with tempfile.NamedTemporaryFile(
        suffix=suffix,
        delete=False,
    ) as temp:

        temp.write(contents)
        temp_path = temp.name

    text = extract_text(temp_path)

    return {
        "filename": file.filename,
        "text": text,
    }