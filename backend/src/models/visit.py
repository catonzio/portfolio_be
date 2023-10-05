from db import Base
from sqlalchemy import Column, Integer, String


class Visit(Base):
    __tablename__ = "visits"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ip = Column(String, index=True)
    city = Column(String)
    region = Column(String)
    country = Column(String)
