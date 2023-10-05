from models.visit import Visit
from sqlalchemy.orm import Session

from schemas.visit_schema import VisitCreate


class VisitRepo:
    async def create_visit(db: Session, visit: VisitCreate) -> Visit:
        db_visit = Visit(
            ip=visit.ip, city=visit.city, region=visit.region, country=visit.country
        )
        db.add(db_visit)
        db.commit()
        db.refresh(db_visit)
        return db_visit

    async def get_all_visits(db: Session) -> list[Visit]:
        db_visits: list[Visit] = db.query(Visit).all()
        return db_visits
