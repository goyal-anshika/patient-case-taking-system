from app.ai.conversation.question_engine import (
    get_next_question,
)


def test_question_engine():

    result = get_next_question(set())

    assert result is not None
    assert result["field"] == "chief_complaint"


def test_question_engine_progress():

    result = get_next_question(
        {
            "chief_complaint",
            "duration",
        }
    )

    assert result is not None
    assert result["field"] == "onset"