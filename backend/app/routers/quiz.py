from fastapi import APIRouter
from app.db import get_db
from app.schemas.question import QuestionOut
from typing import List
from app.schemas.quiz_submit import QuizSubmitRequest
from app.schemas.quiz_result import QuizResult, QuizDetail
from fastapi import Depends
from app.auth import get_current_user
from app.schemas.quiz_session import QuizSessionOut
from app.schemas.wrong_question import WrongQuestionOut
import sqlite3

router = APIRouter(prefix="/quiz", tags=["Quiz"])

@router.get("/questions", response_model=List[QuestionOut])
def get_questions(limit: int = 50):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT id, content, image_url
        FROM questions
        ORDER BY RANDOM()
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    db.close()

    return [dict(row) for row in rows]
@router.post("/submit", response_model=QuizResult)
def submit_quiz(
    data: QuizSubmitRequest,
    current_user = Depends(get_current_user)
):
    db = get_db()
    cursor = db.cursor()

    total = len(data.answers)
    score = 0
    details = []

    user_id = current_user.id

    cursor.execute("""
        INSERT INTO quiz_sessions (user_id, score, total)
        VALUES (?, ?, ?)
    """, (user_id, 0, total))

    session_id = cursor.lastrowid

    for item in data.answers:
        cursor.execute("""
            SELECT correct_answer, explanation
            FROM questions
            WHERE id = ?
        """, (item.question_id,))

        row = cursor.fetchone()
        if not row:
            continue

        correct_answer = bool(row["correct_answer"])
        explanation = row["explanation"]
        is_correct = (item.answer == correct_answer)

        if is_correct:
            score += 1

        cursor.execute("""
            INSERT INTO quiz_answers
            (session_id, question_id, user_answer, is_correct)
            VALUES (?, ?, ?, ?)
        """, (
            session_id,
            item.question_id,
            item.answer,
            is_correct
        ))

        details.append(
            QuizDetail(
                question_id=item.question_id,
                is_correct=is_correct,
                correct_answer=correct_answer,
                explanation=explanation
            )
        )

    cursor.execute("""
        UPDATE quiz_sessions
        SET score = ?
        WHERE id = ?
    """, (score, session_id))

    db.commit()
    db.close()

    return QuizResult(
        score=score,
        total=total,
        details=details
    )
@router.get("/sessions", response_model=list[QuizSessionOut])
def get_my_sessions(
    current_user = Depends(get_current_user)
):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT id, score, total, created_at
        FROM quiz_sessions
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (current_user.id,))

    rows = cursor.fetchall()
    db.close()

    return [dict(row) for row in rows]
@router.get("/wrong-questions", response_model=list[WrongQuestionOut])
def get_wrong_questions(
    current_user = Depends(get_current_user)
):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT DISTINCT
            q.id AS question_id,
            q.content,
            q.image_url,
            q.correct_answer,
            q.explanation
        FROM quiz_answers qa
        JOIN quiz_sessions qs ON qa.session_id = qs.id
        JOIN questions q ON qa.question_id = q.id
        WHERE qs.user_id = ?
          AND qa.is_correct = 0
        ORDER BY q.id
    """, (current_user.id,))

    rows = cursor.fetchall()
    db.close()

    return [dict(row) for row in rows]
