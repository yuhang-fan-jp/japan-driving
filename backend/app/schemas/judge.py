from pydantic import BaseModel
from typing import Optional

class JudgeQuestionCreate(BaseModel):
    content: str
    answer: bool
    analysis: Optional[str] = None
    region: Optional[str] = None
