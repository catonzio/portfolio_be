from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from models.project import Project
from repositories.project_repository import ProjectRepo
from schemas.project_schema import ProjectSchema, ProjectCreate


router = APIRouter(tags=["Projects"])


# method for create projects from a schema input
@router.post("/", response_model=ProjectSchema, status_code=201)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    """Create a project from a schema input"""
    db_project: Project = await ProjectRepo.create_project(db, project)
    return db_project


@router.get("/", response_model=list[ProjectSchema])
async def get_projects(db: Session = Depends(get_db)):
    """Get all projects"""
    db_projects: list[Project] = await ProjectRepo.get_projects(db)
    return db_projects
