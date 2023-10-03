from fastapi import Depends, HTTPException
from app.models.user import User

def get_current_user(username: str = Depends(auth.get_current_username)):
    # 实现用户认证逻辑，验证用户名和令牌等
    user = User(username=username)
    if not user:
        raise HTTPException(status_code=401, detail="用户未授权")
    return user
