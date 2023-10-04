from app.models.email_model import EmailVerifyRequest, EmailVerifyResponse
from app.models.email_model import EmailVerify
from fastapi import APIRouter, HTTPException
from app.utils.email_token import generate, send_verify_token
from app.db.redis import mail_redis_client


router = APIRouter()


@router.post(
        "/send-email", response_model=EmailVerifyResponse
)
async def send_email(request: EmailVerifyRequest):
    email = request.email

    # 生成令牌并存储到Redis
    send_verify_token(email, generate(email))

    # 此处省略发送验证邮件的代码

    return {"message": "Verification email sent successfully."}


@router.post("/confirm-token", response_model=EmailVerifyResponse)
async def confirm_token(token_request: EmailVerify):
    token = token_request.token
    email = token_request.email

    # 从Redis中获取令牌
    key = f'{email}'
    stored_token = mail_redis_client.get(key)

    if stored_token and stored_token.decode('utf-8') == token:  # type: ignore
        # 令牌有效，可以进行邮箱验证
        # 这里可以添加验证成功后的逻辑
        return {"message": "Email verified successfully."}
    else:
        raise HTTPException(status_code=400, detail="Invalid token or email.")
