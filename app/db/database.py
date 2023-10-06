from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy import MetaData

DATABASE_URL = "mysql+mysqlconnector://drawing:Drawingadmin@localhost/drawing"

engine = create_engine(
    DATABASE_URL, pool_size=10, max_overflow=20, echo=True
)

metadata = MetaData()

Base = declarative_base()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def init_db():
    # 尝试创建表，如果数据库不存在则创建
    try:
        Base.metadata.create_all(bind=engine)  # type: ignore
    except OperationalError:
        pass  # 数据库已经存在，不需要再次创建


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
