from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Question, QuestionImage
from app.schemas.question_admin import QuestionBatchCreate

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/questions/batch")
def create_questions_batch(
    data: QuestionBatchCreate,
    db: Session = Depends(get_db),
):
    created_ids = []

    for q in data.questions:
        question = Question(
            content=q.content,
            correct_answer=q.correct_answer,
            explanation=q.explanation,
        )
        db.add(question)
        db.commit()
        db.refresh(question)

        for url in q.images or []:
            img = QuestionImage(
                question_id=question.id,
                image_url=url
            )
            db.add(img)

        db.commit()
        created_ids.append(question.id)

    return {
        "count": len(created_ids),
        "ids": created_ids
    }