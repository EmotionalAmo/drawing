from fastapi import Request


async def log_request(request: Request):
    # 记录请求日志
    logging.info(f"请求路径: {request.url}，请求方法: {request.method}")
