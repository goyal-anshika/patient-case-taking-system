import base64
import json

import httpx

from ..speech_service import SpeechToTextProvider


class AI4BharatSpeechProvider(SpeechToTextProvider):

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    async def transcribe(
        self,
        audio_bytes: bytes,
        language: str,
    ) -> str:

        encoded_audio = base64.b64encode(
            audio_bytes
        ).decode("ascii")

        payload = {
            "config": {
                "language": {
                    "sourceLanguage": language
                },
                "transcriptionFormat": {
                    "value": "transcript"
                },
                "audioFormat": "wav",
                "samplingRate": "16000",
                "postProcessors": None,
            },
            "audio": [
                {
                    "audioContent": encoded_audio
                }
            ],
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/recognize/{language}",
                json=payload,
                timeout=120,
            )

            response.raise_for_status()

            result = response.json()

        return result["output"][0]["source"]