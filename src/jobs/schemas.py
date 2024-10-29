from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class JobUser(BaseModel):
    user_id: int
    name: str


class JobPostBase(BaseModel):
    title: str
    company: str
    location: str


class JobPostCreate(JobPostBase):
    posted_date: str
    description: Optional[str] = None
    url: str


class JobPostResponse(JobPostBase):
    id: int
    posted_date: str
    user: JobUser

    class Config:
        from_attributes = True


class JobPostDetail(JobPostResponse):
    description: Optional[str] = None
    created_at: datetime
    is_active: bool
    is_favorite: bool
    url: str

    class Config:
        from_attributes = True
