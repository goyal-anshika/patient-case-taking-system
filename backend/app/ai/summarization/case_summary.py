import json

import httpx

from app.config import settings


SUMMARY_PROMPT = """
You are a clinical documentation assistant.

Create a concise structured pre-consultation summary
from the information provided.

Rules:
- Do not diagnose.
- Do not invent information.
- Clearly distinguish patient-reported information.
- Preserve uncertainty.
- Do not convert unknown information into facts.
- The doctor must review the final summary.
"""


async def generate_case_summary(
    responses: list[dict],
    ocr_text: str | None = None,
) -> dict:

    context = {
        "patient_responses": responses,
        "document_text": ocr_text or "",
    }

    payload = {
        "model": settings.OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": SUMMARY_PROMPT,
            },
            {
                "role": "user",
                "content": json.dumps(
                    context,
                    ensure_ascii=False,
                ),
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

    return json.loads(
        data["choices"][0]["message"]["content"]
    )