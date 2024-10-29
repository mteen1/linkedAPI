from sqlalchemy.orm import Session
from .schemas import UserBase, UserCreate, UserUpdate
from .models import User

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()


def create_user(db: Session, request: UserCreate):
    new_user = User(
        user_id=request.user_id,
        is_active=request.is_active,
        is_superuser=False,
        password=hash_password(request.password),
        name=request.name,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, request: UserUpdate):
    user = db.query(User).filter(User.user_id == request.user_id).first()
    user.name = request.name
    user.is_active = request.is_active
    user.is_superuser = request.is_superuser
    user.password = hash_password(request.password)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: str):
    user = db.query(User).filter(User.user_id == user_id).first()
    db.delete(user)
    db.commit()
    return user
