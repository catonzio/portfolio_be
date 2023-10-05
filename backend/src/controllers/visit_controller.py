from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from repositories.visit_repository import VisitRepo
from schemas.visit_schema import VisitCreate, VisitSchema
from settings import settings

router = APIRouter(tags=["Visits"])


@router.get("/")
async def get_visits(db: Session = Depends(get_db)):
    return await VisitRepo.get_all_visits(db)


@router.post("/", response_model=VisitSchema | dict)
async def create_visit(
    visit: VisitCreate, db: Session = Depends(get_db)
) -> VisitSchema:
    if visit.ip == settings.personal_ip:
        return {"message": "Visit not saved"}
    return await VisitRepo.create_visit(db, visit)
