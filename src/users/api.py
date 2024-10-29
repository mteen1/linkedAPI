from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from src.users import services
from .schemas import UserCreate, UserResponse, UserUpdate
from .models import User
from typing import List

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
async def get_all_users(db=Depends(get_db)):
    return db.query(User).all()


@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db=Depends(get_db)):
    return services.create_user(db, user)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db=Depends(get_db)):
    user = services.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate, db=Depends(get_db)):
    return services.update_user(db, user)


@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int, db=Depends(get_db)):
    return services.delete_user(db, user_id)
