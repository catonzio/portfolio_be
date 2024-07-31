import json
from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from models.project import Project
from repositories.project_repository import ProjectRepo
from schemas.project_schema import ProjectSchema, ProjectCreate, ProjectUpdate
import requests

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


@router.get("/{project_id}", response_model=ProjectSchema | dict)
async def get_project(project_id: int, db: Session = Depends(get_db)):
    """Get a project by id"""
    db_project: Project = await ProjectRepo.get_project(db, project_id)
    return (
        db_project
        if db_project
        else {"message": f"Project not found with the ID {project_id}"}
    )


@router.put("/{project_id}", response_model=dict)
async def update_project(
    project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)
) -> dict:
    """Update a project by id"""
    db_project: Project = await ProjectRepo.get_project(db, project_id)
    if not db_project:
        return {"message": f"Project not found with the ID {project_id}"}

    await ProjectRepo.update_project(db, project_id, project)
    return {"message": "Project updated"}


@router.delete("/{project_id}", response_model=ProjectSchema | dict)
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    """Delete a project by id"""
    db_project: Project = await ProjectRepo.get_project(db, project_id)
    if not db_project:
        return {"message": f"Project not found with the ID {project_id}"}

    db_project: Project = await ProjectRepo.delete_project(db, project_id)
    return db_project

@router.get("/readme/{project_id}")
async def get_project_readme(project_id: int, db: Session = Depends(get_db)):
    """Get the README of a project from github"""
    project: Project = await ProjectRepo.get_project(db, project_id)
    if not project:
        return {"message": f"Project not found with the ID {project_id}"}
    repo_name = project.github_url.split("/")[-1]
    resp = requests.get(f"https://api.github.com/repos/catonzio/{repo_name}/readme").json()
    readme_url = resp.get('download_url', '')
    print(readme_url)
    return requests.get(readme_url).content