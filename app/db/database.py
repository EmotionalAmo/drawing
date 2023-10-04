from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError  # 导入 OperationalError
import databases

DATABASE_URL = "mysql+mysqlconnector://drawing:Drawingadmin@localhost/drawing"

database = databases.Database(DATABASE_URL)

Base = declarative_base()

engine = create_engine(DATABASE_URL)


# 这里可以添加 create_tables 函数
def create_tables():
    # 尝试创建表，如果数据库不存在则创建
    try:
        Base.metadata.create_all(bind=engine)  # type: ignore
    except OperationalError:
        pass  # 数据库已经存在，不需要再次创建


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db():
    db = database
    try:
        yield db
    finally:
        db.pop()  # type: ignore
