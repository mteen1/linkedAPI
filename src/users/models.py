from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    user_id = Column(Integer, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    password = Column(String)
    job_posts = relationship("JobPost", back_populates="user")
