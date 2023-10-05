from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from controllers.project_controller import router as project_router
from controllers.email_controller import router as email_router
from controllers.visit_controller import router as visit_router
import uvicorn

from db import create_tables


app = FastAPI(
    title="backend Backend",
    description="FastAPI Application backend for backend",
    version="1.0.0",
    docs_url="/portfolio/api/docs",
    openapi_url="/portfolio/api/openapi.json",
)

app.include_router(email_router, prefix="/portfolio/api/email")
app.include_router(project_router, prefix="/portfolio/api/projects")
app.include_router(visit_router, prefix="/portfolio/api/visits")

origins = [
    "http://localhost:56368",  # Add your origins here
    "http://localhost:80"
    # "http://your.other.domain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()


@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(
        status_code=400, content={"message": f"{base_error_message}. Detail: {err}"}
    )


@app.get("/")
async def root():
    return RedirectResponse(url="/portfolio/api")


@app.get("/portfolio/api")
async def root_portfolio():
    return RedirectResponse(url="/portfolio/api/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7000, reload=True)
