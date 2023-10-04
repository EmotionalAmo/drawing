from email.mime.multipart import MIMEMultipart
from app.db.redis import mail_redis_client
from email.mime.text import MIMEText
import smtplib
import random
import string


# 生成验证令牌并存储到Redis
def generate(email):
    token = ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(6)
    )
    key = f'{email}'
    mail_redis_client.setex(key, 300, token)  # 令牌将在5分钟后过期
    return token


def send_verify_token(email, token):
    # 发送验证邮件，这里使用SMTP示例
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"

    subject = "Email Verification"
    message = f"Your verification code is: {token}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, email, msg.as_string())
        return True
    except Exception as e:
        print(f"Failed to send verification email: {e}")
        return False
