from pydantic import BaseModel, EmailStr


class EmailVerifyRequest(BaseModel):
    email: EmailStr


class EmailVerifyResponse(BaseModel):
    message: str


class EmailVerify(BaseModel):
    email: EmailStr
    token: str
