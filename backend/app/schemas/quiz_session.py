from pydantic import BaseModel
from datetime import datetime

class QuizSessionOut(BaseModel):
    id: int
    score: int
    total: int
    created_at: datetime
