from sqlalchemy import Boolean, Column, Integer, String
from db import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String)
    image_path = Column(String)
    url = Column(String)
    preview = Column(Boolean, default=False)
