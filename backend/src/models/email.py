from sqlalchemy import Column, Integer, String
from db import Base


class Email(Base):
    __tablename__ = "emails"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    subject = Column(String, nullable=False)
    sender_email = Column(String, nullable=False)
    sender_name = Column(String, nullable=False)
    body = Column(String, nullable=False)