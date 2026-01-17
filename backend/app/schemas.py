from pydantic import BaseModel, EmailStr
from typing import List

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

class Config:
        from_attributes = True

#class LoginRequest(BaseModel):
#    email: EmailStr
#    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class QuestionImageResponse(BaseModel):
    image_url: str

    class Config:
        from_attributes = True


class QuestionPublic(BaseModel):
    id: int
    content: str
    images: List[QuestionImageResponse]

    class Config:
        from_attributes = True

