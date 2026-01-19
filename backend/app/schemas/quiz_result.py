from pydantic import BaseModel
from typing import List

class QuizDetail(BaseModel):
    question_id: int
    is_correct: bool
    correct_answer: bool
    explanation: str | None

class QuizResult(BaseModel):
    score: int
    total: int
    details: List[QuizDetail]
