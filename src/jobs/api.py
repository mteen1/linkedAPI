from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from config.database import get_db
from src.jobs import services
from .schemas import JobPostCreate, JobPostResponse, JobPostDetail

router = APIRouter()


@router.get("/", response_model=List[JobPostResponse])
async def list_jobs(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return services.get_jobs(db, skip=skip, limit=limit)


@router.post("/{user_id}", response_model=JobPostResponse)
async def create_job(
    job: JobPostCreate,
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    return services.create_job(db, job, user_id)


@router.get("/{user_id}", response_model=list[JobPostResponse])
async def get_user_jobs(user_id: int, db=Depends(get_db)):
    return services.get_jobs(db, user_id=user_id)


@router.get("/detail/{job_id}", response_model=JobPostDetail)
async def get_job_detail(job_id: int, db=Depends(get_db)):
    job = services.get_job(db, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
