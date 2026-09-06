import json
import httpx

from app.config import settings
from .prompts import CLINICAL_EXTRACTION_SYSTEM_PROMPT


async def extract_clinical_information(
    patient_message: str,
) -> dict:

    payload = {
        "model": settings.OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": CLINICAL_EXTRACTION_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": patient_message,
            },
        ],
        "temperature": 0,
    }

    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
        )

        response.raise_for_status()

        data = response.json()

    content = data["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "raw_response": content
        }