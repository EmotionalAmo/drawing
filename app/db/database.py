import mysql.connector
from app.main import app

# 从应用状态中获取数据库连接字符串
db_connection = app.state.db_connection

# 连接到数据库
db = mysql.connector.connect(db_connection)

# 执行数据库操作的函数
def perform_database_query(query):
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
