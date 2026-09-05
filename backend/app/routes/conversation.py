from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.conversation.llm_service import (
    extract_clinical_information,
)


router = APIRouter(
    prefix="/api/ai/conversation",
    tags=["AI - Conversation"],
)


class ConversationRequest(BaseModel):
    text: str


@router.post("/extract")
async def extract_information(
    request: ConversationRequest,
):

    extracted = await extract_clinical_information(
        request.text
    )

    return {
        "input": request.text,
        "extracted": extracted,
    }