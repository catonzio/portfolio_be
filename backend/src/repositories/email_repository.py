from models.email import Email
from schemas.email_schema import EmailSend
from sqlalchemy.orm import Session


class EmailRepo:
    async def create_email(db: Session, email: EmailSend) -> Email:
        db_email: Email = Email(
            subject=email.subject,
            sender_email=email.sender_email,
            sender_name = email.sender_name,
            body=email.body,
        )

        db.add(db_email)
        db.commit()
        db.refresh(db_email)
        return db_email

    async def get_all_emails(db: Session) -> list[Email]:
        db_emails: list[Email] = db.query(Email).all()
        return db_emails
