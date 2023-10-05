from sqlalchemy.orm import Session
from pathlib import Path
import aiosmtplib
from fastapi import APIRouter, Depends
from fastapi_mail import FastMail, MessageSchema
from db import get_db
from repositories.email_repository import EmailRepo
import traceback
from schemas.email_schema import EmailSchema, EmailSend
from settings import Settings


router = APIRouter(tags=["Email"])


@router.post("/send", response_model=dict)
async def send_email(email: EmailSend, db: Session = Depends(get_db)):
    message = MessageSchema(
        subject=email.subject,
        recipients=["danilocatone@gmail.com"],
        template_body={
            "title": "You received a message from " + email.sender_email,
            "content": email.body,
            "name": email.sender_name,
        },
        subtype="html",
    )

    fm = FastMail(
        Settings.conf.model_copy(update={"MAIL_FROM_NAME": email.sender_name})
    )
    try:
        await fm.send_message(message, template_name="email.html")
        await EmailRepo.create_email(db, email)
        return {"message": "Email sent"}
    except aiosmtplib.errors.SMTPDataError as e:
        print(f"SMTP Data Error: {e}")
        print(f"SMTP Response: {e.code} {e.message}")
        return {"message": "Error sending email", "error": str(e)}
    except Exception as e:
        traceback.print_exc()
        return {"message": "Unexpected error", "error": traceback.format_exc()}


@router.get("/", response_model=list[EmailSchema])
async def get_all_emails(db: Session = Depends(get_db)):
    return await EmailRepo.get_all_emails(db)
