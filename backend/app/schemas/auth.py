import uuid

from pydantic import BaseModel, ConfigDict, EmailStr


class RegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str = "doctor"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    full_name: str
    email: EmailStr
    role: str
    is_active: bool


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"