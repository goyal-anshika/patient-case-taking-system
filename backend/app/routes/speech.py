from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import Response

from app.ai.speech.speech_manager import (
    get_stt_provider,
    get_tts_provider,
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
    if language not in {"hi", "en"}:
        return {
            "error": "Unsupported language. Use 'hi' or 'en'."
        }

    audio_bytes = await file.read()

    if not audio_bytes:
        return {
            "error": "Audio file is empty."
        }

    provider = get_stt_provider()

    text = await provider.transcribe(
        audio_bytes,
        language,
    )

    return {
        "language": language,
        "text": text,
    }


@router.post("/synthesize")
async def synthesize_text(
    text: str = Form(...),
    language: str = Form("hi"),
):
    if language not in {"hi", "en"}:
        return {
            "error": "Unsupported language. Use 'hi' or 'en'."
        }

    if not text.strip():
        return {
            "error": "Text cannot be empty."
        }

    provider = get_tts_provider()

    audio_bytes = await provider.synthesize(
        text,
        language,
    )

    return Response(
        content=audio_bytes,
        media_type="audio/mpeg",
    )