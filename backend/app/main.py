import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router


def create_app() -> FastAPI:
    app = FastAPI(title="Search Playground API", version="0.1.0",
        description="Foundation for a visual search lab. Preview and catalog only; game rules and solvers are not implemented.")
    origins = os.getenv("FRONTEND_ORIGINS", "http://localhost:5174,http://127.0.0.1:5174")
    app.add_middleware(CORSMiddleware,
        allow_origins=[origin.strip() for origin in origins.split(",") if origin.strip()],
        allow_methods=["GET"], allow_headers=["Content-Type"])
    app.include_router(router)
    return app


app = create_app()
