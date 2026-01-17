from pydantic import BaseModel

class QuestionPublic(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True  # 后面接 SQLAlchemy