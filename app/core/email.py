from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME"),
    MAIL_TLS=True,
    MAIL_SSL=False,
)

async def send_registration_email(email: EmailStr, username: str):
    template = Path(__file__).parent / "templates" / "welcome_email.html"
    with open(template) as f:
        template_str = f.read()

    message = MessageSchema(
        subject="Welcome to User Management API",
        recipients=[email],
        body=template_str.format(username=username),
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
