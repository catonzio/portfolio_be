from pydantic import BaseModel

class VisitBase(BaseModel):
    ip: str
    city: str
    region: str
    country: str
    
class VisitCreate(VisitBase):
    pass

class VisitSchema(VisitBase):
    id: int

    class Config:
        from_attributes = True
        # orm_mode = True