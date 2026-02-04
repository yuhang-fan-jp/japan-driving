from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Question, QuestionImage, JudgeQuestion
from app.schemas import JudgeQuestionCreate
from app.schemas.question_admin import QuestionBatchCreate
from app.auth import get_current_user, get_admin_user
from app import schemas, models

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/questions/batch")
def create_questions_batch(
    data: QuestionBatchCreate,
    db: Session = Depends(get_db),
    admin = Depends(get_admin_user),
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

@router.post("/admin/import-judge-questions")
def import_judge_questions(
    questions: list[schemas.JudgeQuestionCreate],
    db: Session = Depends(get_db),
    admin=Depends(get_current_user),
):
    for q in questions:
        question = models.Question(
            content=q.content,
            answer=q.answer,      # boolean
            analysis=q.analysis,
            region=q.region,
            type="judge",        
        )
        db.add(question)
        db.flush()

        for img_url in q.images:
            db.add(models.QuestionImage(
                question_id=question.id,
                image_url=img_url
            ))

    db.commit()
    return {"count": len(questions)}

@router.post("/judge/batch")
def import_judge_questions(
    questions: list[JudgeQuestionCreate],
    db: Session = Depends(get_db),
    admin=Depends(get_admin_user),
):
    for q in questions:
        db.add(JudgeQuestion(
            content=q.content,
            answer=q.answer,
            analysis=q.analysis,
            region=q.region,
        ))
    db.commit()

    return {"count": len(questions)}