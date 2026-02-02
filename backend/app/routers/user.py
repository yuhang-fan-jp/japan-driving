from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app import models
from app.database import get_db
from app.models import User
from app.schemas.user import UserProfileUpdate, ChangePassword
from app.auth import get_current_user
from app.security import verify_password, hash_password

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/me")
def get_me(user: User = Depends(get_current_user)):
    return {
        "email": user.email,
        "nickname": user.nickname,
        "exam_region": user.exam_region,
    }

@router.post("/profile")
def update_profile(
    data: schemas.UserProfileUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    current_user.nickname = data.nickname
    current_user.exam_region = data.exam_region

    db.commit()
    db.refresh(current_user)

    return {
        "id": current_user.id,
        "email": current_user.email,
        "nickname": current_user.nickname,
        "exam_region": current_user.exam_region,
    }

@router.post("/change-password")
def change_password(
    data: ChangePassword,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if not verify_password(data.old, user.password):
        raise HTTPException(status_code=400, detail="原密码错误")

    user.password = hash_password(data.new)
    db.commit()

    return {"ok": True}