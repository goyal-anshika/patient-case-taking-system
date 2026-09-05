from fastapi import APIRouter, File, Form, UploadFile

from app.ai.speech.providers.mock import (
    MockSpeechProvider,
)


router = APIRouter(
    prefix="/api/ai/speech",
    tags=["AI - Speech"],
)


@router.post("/transcribe")
async def transcribe_audio(
    file: UploadFile = File(...),
    language: str = Form("hi"),
):

    audio_bytes = await file.read()

    provider = MockSpeechProvider()

    text = await provider.transcribe(
        audio_bytes,
        language,
    )

    return {
        "language": language,
        "text": text,
    }