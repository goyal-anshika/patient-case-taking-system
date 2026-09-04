from fastapi import HTTPException


def not_found(resource: str) -> HTTPException:
    return HTTPException(
        status_code=404,
        detail=f"{resource} not found",
    )


def unauthorized(
    message: str = "Unauthorized",
) -> HTTPException:
    return HTTPException(
        status_code=401,
        detail=message,
    )