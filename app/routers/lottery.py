from redis import Redis
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends


router = APIRouter()


# 接受用户投注
@router.post("/bet/")
async def bet():
    return None


# 生成开奖号码
@router.post("/generate/")
async def generate():
    return None


# 查看开奖情况
@router.post("/check/")
async def check():
    return None
