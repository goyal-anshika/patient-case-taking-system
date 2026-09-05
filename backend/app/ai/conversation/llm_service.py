import json

import httpx

from app.config import settings


SYSTEM_PROMPT = """
You are a clinical case-taking assistant.

Your role is to help collect and structure patient-provided
information before a doctor consultation.

Rules:
1. Do not diagnose.
2. Do not prescribe medicines.
3. Do not invent symptoms.
4. Extract only information supported by the patient input.
5. Ask focused follow-up questions.
6. Keep patient information in structured fields.
7. The doctor remains the final clinical decision maker.
"""


async def extract_clinical_information(
    patient_text: str,
) -> dict:

    if not settings.OPENROUTER_API_KEY:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not configured"
        )

    payload = {
        "model": settings.OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": patient_text,
            },
        ],
        "response_format": {
            "type": "json_object"
        },
    }

    headers = {
        "Authorization": (
            f"Bearer {settings.OPENROUTER_API_KEY}"
        ),
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

    content = data["choices"][0]["message"]["content"]

    return json.loads(content)