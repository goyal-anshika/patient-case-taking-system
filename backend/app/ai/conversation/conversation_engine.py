from typing import Any

from app.ai.conversation.llm_service import (
    extract_clinical_information,
)
from app.ai.conversation.question_engine import (
    get_next_question,
)


SUPPORTED_LANGUAGES = {"en", "hi"}


async def process_message(
    text: str,
    state: dict[str, Any] | None = None,
    language: str = "en",
) -> dict[str, Any]:

    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(
            "Unsupported language. Use 'en' or 'hi'."
        )

    if not text or not text.strip():
        raise ValueError("Message cannot be empty.")

    current_state = dict(state or {})

    # --------------------------------------------------
    # 1. Extract clinical information from patient text
    # --------------------------------------------------

    extracted = await extract_clinical_information(text)

    # Pydantic model → dictionary if necessary
    if hasattr(extracted, "model_dump"):
        extracted = extracted.model_dump()

    elif not isinstance(extracted, dict):
        extracted = dict(extracted)

    # --------------------------------------------------
    # 2. Update conversation state
    # --------------------------------------------------

    for field, value in extracted.items():

        if value is None:
            continue

        if value == "":
            continue

        if value == []:
            continue

        current_state[field] = value

    # --------------------------------------------------
    # 3. Determine next question
    # --------------------------------------------------

    next_question = get_next_question(current_state)

    # --------------------------------------------------
    # 4. Conversation completed
    # --------------------------------------------------

    if next_question is None:

        response_text = (
            "Thank you. I have collected the information "
            "needed for your consultation."
            if language == "en"
            else
            "धन्यवाद। मैंने आपकी परामर्श के लिए "
            "आवश्यक जानकारी एकत्र कर ली है।"
        )

        return {
            "language": language,
            "input_text": text,
            "extracted": extracted,
            "state": current_state,
            "response_text": response_text,
            "next_field": None,
            "next_question": None,
            "completed": True,
        }

    # --------------------------------------------------
    # 5. Continue controlled conversation
    # --------------------------------------------------

    question_text = next_question["question"]

    # Hindi translation for ontology questions.
    # We keep the clinical field controlled by the ontology.
    if language == "hi":

        hindi_questions = {
            "chief_complaint":
                "आज आपको मुख्य समस्या क्या हो रही है?",

            "location":
                "यह समस्या आपको शरीर के किस हिस्से में हो रही है?",

            "onset":
                "यह समस्या कब शुरू हुई?",

            "duration":
                "आपको यह समस्या कितने समय से है?",

            "character":
                "आप इस समस्या को किस तरह महसूस करते हैं?",

            "aggravating_factors":
                "क्या कोई चीज़ इस समस्या को और बढ़ा देती है?",

            "relieving_factors":
                "क्या कोई चीज़ इस समस्या को कम करती है?",

            "associated_symptoms":
                "क्या इसके साथ आपको कोई और लक्षण भी हो रहे हैं?",
        }

        question_text = hindi_questions.get(
            next_question["field"],
            question_text,
        )

    return {
        "language": language,
        "input_text": text,
        "extracted": extracted,
        "state": current_state,
        "response_text": question_text,
        "next_field": next_question["field"],
        "next_question": question_text,
        "completed": False,
    }