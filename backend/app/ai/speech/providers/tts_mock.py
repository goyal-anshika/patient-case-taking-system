from ..speech_service import TextToSpeechProvider


class MockTTSProvider(TextToSpeechProvider):

    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> bytes:

        # Temporary mock audio response.
        # Real TTS provider will replace this later.
        return b""