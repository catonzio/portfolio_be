from schemas.project_schema import ProjectCreate
from models.project import Project
from sqlalchemy.orm import Session


class ProjectRepo:
    async def create_project(db: Session, project: ProjectCreate) -> Project:
        db_project = Project(
            name=project.name,
            description=project.description,
            image_path=project.image_path,
            url=project.url,
            preview=project.preview,
        )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

    async def get_project(db: Session, project_id: int) -> Project:
        db_project = db.query(Project).filter(Project.id == project_id).first()
        return db_project

    async def get_projects(db: Session) -> list[Project]:
        db_projects = db.query(Project).all()
        return db_projects
