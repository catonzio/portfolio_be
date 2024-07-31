from typing import Any
from pydantic import BaseModel
from schemas.project_schema import ProjectCreate, ProjectUpdate
from models.project import Project
from sqlalchemy.orm import Session


class ProjectRepo:
    async def create_project(db: Session, project: ProjectCreate) -> Project:
        db_project: Project = Project(
            name=project.name,
            description=project.description,
            image_path=project.image_path,
            url=project.url,
            github_url=project.github_url,
            preview=project.preview,
        )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

    async def get_project(db: Session, project_id: int) -> Project:
        db_project: Project = db.query(Project).filter(Project.id == project_id).first()
        return db_project

    async def get_projects(db: Session) -> list[Project]:
        db_projects: list[Project] = db.query(Project).all()
        return db_projects

    async def update_project(db: Session, project_id: int, project: ProjectUpdate) -> None:
        db.query(Project).filter(Project.id == project_id).update(
            model_update_json(project)
        )
        db.commit()

    async def delete_project(db: Session, project_id: int) -> Project:
        db_project: Project = db.query(Project).filter(Project.id == project_id).first()
        db.delete(db_project)
        db.commit()
        return db_project


def model_update_json(schema: BaseModel) -> dict[str, Any]:
    return {k: v for k, v in schema.model_dump().items() if v is not None}
