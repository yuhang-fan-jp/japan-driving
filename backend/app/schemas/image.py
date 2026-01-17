from pydantic import BaseModel

class ImageUploadRequest(BaseModel):
    question_id: int
    filename: str
    content_type: str
