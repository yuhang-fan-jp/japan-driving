from sqlalchemy import (
    Column, Integer, String, DateTime,
    Boolean, ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


# =====================
# 用户
# =====================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    nickname = Column(String, default="")
    avatar_url = Column(String, default="")

    created_at = Column(DateTime, default=datetime.utcnow)

    sessions = relationship("QuizSession", back_populates="user")


# =====================
# 题目（判断题）
# =====================
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    correct_answer = Column(Boolean, nullable=False)

    explanation = Column(String, default="")  # 解析
    created_at = Column(DateTime, default=datetime.utcnow)

    images = relationship("QuestionImage", back_populates="question")
    answers = relationship("QuizAnswer", back_populates="question")


# =====================
# 题目图片
# =====================
class QuestionImage(Base):
    __tablename__ = "question_images"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    image_url = Column(String, nullable=False)

    question = relationship("Question", back_populates="images")


# =====================
# 一次练习 / 考试记录
# =====================
class QuizSession(Base):
    __tablename__ = "quiz_sessions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    total = Column(Integer, nullable=False)        # 题目数
    score = Column(Integer, nullable=False)        # 得分
    duration_sec = Column(Integer, nullable=False) # 用时（秒）

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="sessions")
    answers = relationship("QuizAnswer", back_populates="session")


# =====================
# 每一题的作答
# =====================
class QuizAnswer(Base):
    __tablename__ = "quiz_answers"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("quiz_sessions.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))

    user_answer = Column(Boolean, nullable=False)
    is_correct = Column(Boolean, nullable=False)

    session = relationship("QuizSession", back_populates="answers")
    question = relationship("Question", back_populates="answers")