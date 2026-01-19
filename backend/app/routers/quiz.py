from fastapi import APIRouter
from app.db import get_db
from app.schemas.question import QuestionOut
from typing import List
from app.schemas.quiz_submit import QuizSubmitRequest
from app.schemas.quiz_result import QuizResult, QuizDetail
from fastapi import Depends

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
def submit_quiz(data: QuizSubmitRequest):
    db = get_db()
    cursor = db.cursor()

    total = len(data.answers)
    score = 0
    details = []

    # ⚠️ 现在先写死 user_id = 1（等会再接登录）
    user_id = 1

    # 先创建一次刷题记录（占位）
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

    # 更新最终分数
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
