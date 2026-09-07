from app.ai.speech.providers.ai4bharat import AI4BharatSpeechProvider
from app.config import settings

from app.ai.speech.providers.mock import MockSpeechProvider
from app.ai.speech.providers.tts_mock import MockTTSProvider


def get_stt_provider():

    if settings.SPEECH_PROVIDER == "mock":
        return MockSpeechProvider()

    if settings.SPEECH_PROVIDER == "ai4bharat":
        return AI4BharatSpeechProvider()

    raise ValueError(
        f"Unsupported STT provider: {settings.SPEECH_PROVIDER}"
    )


def get_tts_provider():

    if settings.TTS_PROVIDER == "mock":
        return MockTTSProvider()

    raise ValueError(
        f"Unsupported TTS provider: {settings.TTS_PROVIDER}"
    )