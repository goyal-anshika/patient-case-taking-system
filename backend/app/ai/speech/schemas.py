from pydantic import BaseModel
from typing import Optional


class SpeechToTextResult(BaseModel):
    text: str
    language: str
    confidence: Optional[float] = None


class TextToSpeechResult(BaseModel):
    audio_base64: str
    language: str


class VoiceConversationRequest(BaseModel):
    session_id: str
    language: Optional[str] = None


class VoiceConversationResponse(BaseModel):
    session_id: str
    language: str
    patient_text: str
    response_text: str
    audio_base64: Optional[str] = None
    next_question: Optional[dict] = None