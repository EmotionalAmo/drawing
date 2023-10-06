from sqlalchemy import Column, Integer, String, Boolean, Float
from pydantic import BaseModel, EmailStr
from sqlalchemy_utils import UUIDType

from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUIDType(binary=False), primary_key=True, unique=True)
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


class UserLoginResponse(BaseModel):
    token: str
    message: str


class UserLogout(BaseModel):
    username: str
    token: str


class EmailVerifyRequest(BaseModel):
    email: EmailStr


class EmailVerifyResponse(BaseModel):
    message: str


class EmailVerify(BaseModel):
    email: EmailStr
    token: str
