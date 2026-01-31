# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserProfileUpdate(BaseModel):
    nickname: Optional[str] = Field(None, max_length=20)
    exam_region: Optional[str] = None


class ChangePassword(BaseModel):
    old: str
    new: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"