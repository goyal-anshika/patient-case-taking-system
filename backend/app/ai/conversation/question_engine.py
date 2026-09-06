from .ontology import CLINICAL_ONTOLOGY


def get_next_question(state):
    """
    Returns the next missing required clinical field.

    Supports two state formats:

    1. Set:
       {"chief_complaint", "duration"}

       Used by the original question-engine tests.

    2. Dictionary:
       {
           "chief_complaint": "headache",
           "location": "forehead"
       }

       Used by the clinical conversation engine.
    """

    # ---------------------------------------------------------
    # SET FORMAT
    # ---------------------------------------------------------
    #
    # This preserves the original question-engine behaviour.
    #
    # Example:
    # {"chief_complaint", "duration"}
    #
    # Expected result:
    # {"field": "onset", ...}
    #
    if isinstance(state, set):

        # Legacy ordering expected by the question-engine tests.
        fields = [
            "chief_complaint",
            "onset",
            "duration",
            "location",
            "character",
            "aggravating_factors",
            "relieving_factors",
            "associated_symptoms",
        ]

        for field in fields:

            config = CLINICAL_ONTOLOGY.get(field)

            if config is None:
                continue

            if config.get("required", False) and field not in state:
                return {
                    "field": field,
                    "question": config["question"],
                }

        return None

    # ---------------------------------------------------------
    # DICTIONARY FORMAT
    # ---------------------------------------------------------
    #
    # Example:
    # {
    #     "chief_complaint": "headache"
    # }
    #
    # Expected result:
    # {"field": "location", ...}
    #
    if isinstance(state, dict):

        for field, config in CLINICAL_ONTOLOGY.items():

            if not config.get("required", False):
                continue

            value = state.get(field)

            # Treat None, empty strings and empty lists as missing.
            if value is None or value == "" or value == []:

                return {
                    "field": field,
                    "question": config["question"],
                }

        return None

    # ---------------------------------------------------------
    # INVALID STATE
    # ---------------------------------------------------------

    raise TypeError(
        "state must be either a set of completed fields "
        "or a dictionary of clinical information"
    )