from app.ai.conversation.llm_service import (
    extract_clinical_information,
)


async def extract_entities(
    ocr_text: str,
) -> dict:

    if not ocr_text.strip():
        return {}

    return await extract_clinical_information(
        ocr_text
    )