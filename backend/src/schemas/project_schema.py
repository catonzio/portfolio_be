from typing import Optional
from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    description: str
    image_path: str
    url: str
    preview: bool


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    name: Optional[str] = None
    description: Optional[str] = None
    image_path: Optional[str] = None
    url: Optional[str] = None
    preview: Optional[bool] = None


class ProjectSchema(ProjectBase):
    id: int

    class Config:
        from_attributes = True
        # orm_mode = True
