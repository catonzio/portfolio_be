from pydantic import BaseModel


class EmailBase(BaseModel):
    subject: str
    sender_email: str
    sender_name: str
    body: str


class EmailSend(EmailBase):
    pass


class EmailSchema(EmailBase):
    id: int

    class Config:
        from_attributes = True
        # orm_mode = True
