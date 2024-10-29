from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.jobs.models import JobPost
from src.jobs.schemas import JobPostCreate
from typing import List


def get_jobs(
    db: AsyncSession, skip: int = 0, limit: int = 100, user_id: int = None
) -> List[JobPost]:
    query = select(JobPost).offset(skip).limit(limit)
    if user_id:
        query = query.where(JobPost.user_id == user_id)
    result = db.execute(query)
    return result.scalars().all()


def create_job(db: Session, job: JobPostCreate, user_id: int) -> JobPost:
    db_job = JobPost(**job.dict(), user_id=user_id)
    db.add(db_job)
    try:
        db.commit()
        db.refresh(db_job)
        return db_job
    except Exception as e:
        db.rollback()
        raise e


def get_job(db: AsyncSession, job_id: int) -> JobPost:
    query = select(JobPost).where(JobPost.id == job_id)
    result = db.execute(query)
    return result.scalars().first()
