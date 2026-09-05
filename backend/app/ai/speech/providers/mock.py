from ..speech_service import SpeechToTextProvider


class MockSpeechProvider(SpeechToTextProvider):

    async def transcribe(
        self,
        audio_bytes: bytes,
        language: str,
    ) -> str:

        return "I have had a headache for three days."