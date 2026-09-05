def normalize_confidence(
    value: float | None,
) -> float | None:

    if value is None:
        return None

    return max(
        0.0,
        min(1.0, value),
    )