from pydantic import BaseModel


class EmailBase(BaseModel):
    subject: str
    sender: str
    body: str


class EmailSend(EmailBase):
    pass


class Email(EmailBase):
    id: str

    class Config:
        from_attributes = True
        # orm_mode = True
