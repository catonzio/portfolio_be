from models.email import Email
from schemas.email_schema import EmailSend
from sqlalchemy.orm import Session


class EmailRepo:
    async def create_email(db: Session, email: EmailSend):
        db_email = Email(
            subject=email.subject,
            sender=email.sender,
            body=email.body,
        )

        db.add(db_email)
        db.commit()
        db.refresh(db_email)
        return db_email
