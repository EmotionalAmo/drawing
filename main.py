from fastapi import FastAPI
import logging
import configparser

app = FastAPI()

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 获取数据库连接信息
db_config = config['database']

db_host = db_config['host']
db_user = db_config['user']
db_password = db_config['password']
db_database_name = db_config['database_name']

# 构建数据库连接字符串
db_connection = f"mysql://{db_user}:{db_password}@{db_host}/{db_database_name}"

# 在 FastAPI 应用中使用数据库连接字符串
app.state.db_connection = db_connection

# 导入路由模块
from app.routers import users, lottery

# 注册路由
app.include_router(users.router)
app.include_router(lottery.router)
