from fastapi import APIRouter

router = APIRouter()


@router.get("/users/")
async def get_users():
    # 处理用户相关路由
    return {"message": "获取用户列表"}
