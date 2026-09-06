from app.ai.conversation.question_engine import get_next_question


def test_next_question():

    state = {
        "chief_complaint": "headache"
    }

    result = get_next_question(state)

    assert result is not None
    assert result["field"] == "location"


def test_conversation_completion():

    state = {
        "chief_complaint": "headache",
        "location": "forehead",
        "onset": "yesterday",
        "duration": "one day",
        "character": "throbbing",
    }

    result = get_next_question(state)

    assert result is None