from app.ai.speech.providers.mock import MockSpeechProvider
from app.config import settings


def get_speech_provider():

    if settings.SPEECH_PROVIDER == "mock":
        return MockSpeechProvider()

    raise ValueError(
        f"Unsupported speech provider: "
        f"{settings.SPEECH_PROVIDER}"
    )