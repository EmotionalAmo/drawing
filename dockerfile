# 基础镜像
FROM python:3.11.5

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . .

# 安装依赖包
RUN pip install -r requirements.txt

# 启动应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
