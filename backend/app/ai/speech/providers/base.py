from abc import ABC, abstractmethod
from typing import BinaryIO

from app.ai.speech.schemas import SpeechToTextResult


class SpeechToTextProvider(ABC):

    @abstractmethod
    async def transcribe(
        self,
        audio_file: BinaryIO,
        language: str | None = None,
    ) -> SpeechToTextResult:
        pass

from app.ai.speech.schemas import TextToSpeechResult


class TextToSpeechProvider(ABC):

    @abstractmethod
    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> TextToSpeechResult:
        pass       