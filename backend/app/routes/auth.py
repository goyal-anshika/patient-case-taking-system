from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.security import get_current_user
from ..database import get_db
from ..models.user import User
from ..schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from ..services.auth_service import (
    create_access_token,
    get_user_by_email,
    hash_password,
    verify_password,
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db),
):

    existing_user = get_user_by_email(
        db,
        data.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    user = User(
        full_name=data.full_name,
        email=data.email,
        password_hash=hash_password(data.password),
        role=data.role,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db),
):

    user = get_user_by_email(
        db,
        data.email,
    )

    if not user or not verify_password(
        data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_access_token(
        user.id,
        user.role,
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user