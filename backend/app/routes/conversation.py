from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

from app.ai.conversation.llm_service import (
    extract_clinical_information
)

from app.ai.conversation.question_engine import (
    get_next_question
)


router = APIRouter(
    prefix="/api/ai/conversation",
    tags=["AI Conversation"],
)


class ConversationRequest(BaseModel):
    message: str
    state: Dict[str, Any] = {}


@router.post("/continue")
async def continue_conversation(
    request: ConversationRequest
):

    extracted = await extract_clinical_information(
        request.message
    )

    state = request.state.copy()

    for field, value in extracted.items():

        if field in state and value:
            state[field] = value

    next_question = get_next_question(state)

    return {
        "message": request.message,
        "extracted": extracted,
        "state": state,
        "next_question": next_question,
        "completed": next_question is None,
    }