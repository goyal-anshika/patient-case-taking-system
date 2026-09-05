from .ontology import CLINICAL_FIELDS, QUESTION_MAP


def get_next_question(collected_fields: set[str]) -> dict | None:

    for field in CLINICAL_FIELDS:

        if field not in collected_fields:

            return {
                "field": field,
                "question": QUESTION_MAP[field],
            }

    return None