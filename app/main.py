from fastapi import FastAPI
from app.routers import users, verify
from app.db.database import create_tables

app = FastAPI()

# 初始化数据库表
create_tables()


# ... 其他路由和功能 ...

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(verify.router, prefix="/verify", tags=["verify"])
