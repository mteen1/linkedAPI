from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base


class JobPost(Base):
    __tablename__ = "job_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    location = Column(String)
    description = Column(String)
    url = Column(String)
    posted_date = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_favorite = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship("User", back_populates="job_posts")

    def __repr__(self):
        return f"<JobPost {self.title}>"
