from app.routers import users
from app.db.database import init_db

from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    init_db()
    pass


@app.on_event("shutdown")
async def on_shutdown():
    pass


# ... 其他路由和功能 ...

app.include_router(users.router, prefix="/users")
