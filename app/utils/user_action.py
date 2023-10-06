from app.models.user_model import User, UserCreate
from sqlalchemy.orm import Session

import uuid
import hashlib
from sqlalchemy import select, insert


# 生成UUID
def uuid_generator(db: Session):
    while True:
        uid = uuid.uuid4()
        stmt = select(User).where(User.id == uid)
        result = db.execute(stmt)
        if not result.scalar_one_or_none():
            print(uid, type(uid))
            return str(uid)


def get_user(username: str, db: Session):
    stmt = select(User).where(User.username == username)
    result = db.execute(stmt)
    user = result.scalar_one_or_none()
    return user


def create_user(user: UserCreate, db: Session):
    # 对密码进行哈希处理
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()

    # 插入新用户到数据库
    stmt = insert(User).values(
        id=uuid_generator(db),
        email=user.email,
        username=user.username,
        password=hashed_password,
    )

    # 执行插入操作，但不需要返回结果
    db.execute(stmt)
    db.commit()

    # 返回创建的用户数据，这里不需要获取ID
    created_user = {**user.model_dump()}
    return created_user
