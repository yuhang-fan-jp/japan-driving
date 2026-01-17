from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base
from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    correct_answer = Column(Boolean, nullable=False)
    explanation = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    images = relationship("QuestionImage", back_populates="question")

class QuestionImage(Base):
    __tablename__ = "question_images"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    image_url = Column(String, nullable=False)

    question = relationship("Question", back_populates="images")