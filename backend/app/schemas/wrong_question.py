from pydantic import BaseModel
from typing import Optional

class WrongQuestionOut(BaseModel):
    question_id: int
    content: str
    image_url: Optional[str]
    correct_answer: bool
    explanation: str
