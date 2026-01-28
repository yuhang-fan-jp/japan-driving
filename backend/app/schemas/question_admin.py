from pydantic import BaseModel
from typing import List, Optional

class QuestionItem(BaseModel):
    content: str
    correct_answer: bool
    explanation: str
    images: Optional[List[str]] = []

class QuestionBatchCreate(BaseModel):
    questions: List[QuestionItem]