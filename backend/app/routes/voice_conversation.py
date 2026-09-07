from fastapi import (
    APIRouter,
    File,
    Form,
    UploadFile,
)
from fastapi.responses import Response

from app.ai.speech.speech_manager import (
    get_stt_provider,
    get_tts_provider,
)

from app.ai.conversation.conversation_engine import (
    process_message,
)


router = APIRouter(
    prefix="/api/ai/voice",
    tags=["AI - Voice Conversation"],
)


@router.post("/conversation")
async def voice_conversation(
    file: UploadFile = File(...),
    language: str = Form("en"),
    state: str = Form("{}"),
):

    if language not in {"en", "hi"}:
        return {
            "error": "Unsupported language. Use 'en' or 'hi'."
        }

    # --------------------------------------------------
    # Parse conversation state
    # --------------------------------------------------

    import json

    try:
        conversation_state = json.loads(state)
    except json.JSONDecodeError:
        return {
            "error": "Invalid conversation state."
        }

    # --------------------------------------------------
    # Read audio
    # --------------------------------------------------

    audio_bytes = await file.read()

    if not audio_bytes:
        return {
            "error": "Empty audio file."
        }

    # --------------------------------------------------
    # Speech → Text
    # --------------------------------------------------

    stt_provider = get_stt_provider()

    patient_text = await stt_provider.transcribe(
        audio_bytes,
        language,
    )

    # --------------------------------------------------
    # Text → Clinical Conversation
    # --------------------------------------------------

    conversation_result = await process_message(
        text=patient_text,
        state=conversation_state,
        language=language,
    )

    # --------------------------------------------------
    # Text → Speech
    # --------------------------------------------------

    tts_provider = get_tts_provider()

    response_text = conversation_result["response_text"]

    response_audio = await tts_provider.synthesize(
        response_text,
        language,
    )

    # --------------------------------------------------
    # Return JSON metadata + audio
    # --------------------------------------------------

    # For MVP, return metadata.
    # Audio will be exposed through a separate endpoint
    # in the next step.

    return {
        "language": language,
        "transcript": patient_text,
        "response_text": response_text,
        "next_field": conversation_result["next_field"],
        "completed": conversation_result["completed"],
        "state": conversation_result["state"],
        "audio_available": bool(response_audio),
    }