from abc import ABC, abstractmethod


class SpeechToTextProvider(ABC):

    @abstractmethod
    async def transcribe(
        self,
        audio_bytes: bytes,
        language: str,
    ) -> str:
        raise NotImplementedError


class TextToSpeechProvider(ABC):

    @abstractmethod
    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> bytes:
        raise NotImplementedError