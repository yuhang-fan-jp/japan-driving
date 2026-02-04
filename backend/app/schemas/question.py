from pydantic import BaseModel
from pydantic import BaseModel
from typing import Optional, List

class QuestionPublic(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True  # 后面接 SQLAlchemy

class QuestionOut(BaseModel):
    id: int
    content: str
    image_url: Optional[str]

class JudgeQuestionCreate(BaseModel):
    content: str
    answer: bool
    analysis: str
    images: List[str] = []
    region: str | None = None