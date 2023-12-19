from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from controllers.project_controller import router as project_router
from controllers.email_controller import router as email_router
from controllers.visit_controller import router as visit_router
import uvicorn

from db import create_tables


app = FastAPI(
    root_path="/portfolio/api",
    title="backend Backend",
    description="FastAPI Application backend for backend",
    version="1.0.0",
    # docs_url="/docs",
    # openapi_url="/openapi.json",
)

app.include_router(email_router, prefix="/email")
app.include_router(project_router, prefix="/projects")
app.include_router(visit_router, prefix="/visits")

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
    return RedirectResponse(url="/portfolio/api/docs")

# @app.get("/")
# async def root():
#     return RedirectResponse(url="")


# @app.get("/api")
# async def root_portfolio(request: Request):
#     # return {
#     #     "message": "Hello World",
#     #     "root_path": request.scope.get("root_path"),
#     #     "docs_url": request.scope.get("docs_url"),
#     # }

#     return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=7000,
        reload=True,  # , root_path="/portfolio/api"
    )
