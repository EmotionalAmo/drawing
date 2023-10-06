from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from hashlib import sha256
from os import urandom
from redis import Redis

from app.db.redis import get_redis
from app.db.database import get_db

from app.models.user_model import UserCreate
from app.models.user_model import EmailVerifyRequest, EmailVerifyResponse
from app.models.user_model import UserLogin, UserLoginResponse, UserLogout

from app.utils.email import send_verify_token, generate_email_token
from app.utils.user_action import create_user, get_user


router = APIRouter()


# 注册路由
@router.post("/register/")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user(user.username, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    create_user(user, db)
    return {"detail": "User created successfully"}


# 发送验证邮件
@router.post("/send-email", response_model=EmailVerifyResponse)  # 发送验证邮件
async def send_email(
    request: EmailVerifyRequest, redis: Redis = Depends(get_redis)
):
    email = request.email
    # 生成令牌并存储到Redis发送验证邮件
    send_verify_token(email, generate_email_token(email, redis))
    return {"message": "Verification email sent successfully."}


# 登陆路由
@router.post("/login/", response_model=UserLoginResponse)
async def login(
    user: UserLogin,
    db: Session = Depends(get_db), redis: Redis = Depends(get_redis)
):
    token = redis.get(user.username)
    if not token:
        existing_user = get_user(user.username, db)
        hashed_password = sha256(user.password.encode()).hexdigest()
        if not existing_user or hashed_password != existing_user.password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = sha256(urandom(1024)).hexdigest()
        redis.set(user.username, token, ex=3600)
        return {"token": token, "message": "Logged in successfully"}
    else:
        redis.expire(user.username, 3600)
        return {"token": token, "message": "Already loggin"}


# 注销路由
@router.post("/logout/")
async def logout(user: UserLogout, redis: Redis = Depends(get_redis)):
    if redis.get(user.username).decode('utf-8') == user.token:  # type: ignore
        redis.delete(user.username)
        return {"message": "Logged out successfully"}
    else:
        raise HTTPException(status_code=400, detail="User already logout")
