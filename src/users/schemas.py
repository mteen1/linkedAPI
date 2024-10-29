from pydantic import BaseModel
from typing import Optional
from src.jobs.schemas import JobPostResponse


class UserBase(BaseModel):
    user_id: int
    name: str


class UserCreate(UserBase):
    is_active: bool
    is_superuser: bool
    password: str


class UserResponse(UserBase):
    name: Optional[str] = None
    is_active: bool
    is_superuser: bool
    job_posts: list[JobPostResponse] = []

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    password: Optional[str] = None
