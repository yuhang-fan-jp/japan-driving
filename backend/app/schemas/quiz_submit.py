from pydantic import BaseModel
from typing import List

class AnswerItem(BaseModel):
    question_id: int
    answer: bool

class QuizSubmitRequest(BaseModel):
    answers: List[AnswerItem]
