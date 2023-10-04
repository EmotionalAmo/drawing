from sqlalchemy import Column, String, Integer, Float, Boolean
from pydantic import BaseModel, EmailStr
from app.db.database import Base
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(
        String(36), primary_key=True, unique=True, default=str(uuid.uuid4())
    )
    email = Column(String(100), index=True)
    verify = Column(Boolean, default=False)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(100))
    login_attempts = Column(Integer, default=0)
    balance = Column(Float, default=0.0)


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
