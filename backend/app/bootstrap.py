from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from sqlalchemy import text

from app.settings import settings
from app.db import get_engine
from app.dal import register_models, get_metadata
from app.api.main import api_router

def db_create():
    metadata = get_metadata()
    metadata.create_all(get_engine())

def db_drop():
    metadata = get_metadata()
    metadata.drop_all(get_engine())

def create_app() -> FastAPI:
    def custom_generate_unique_id(route: APIRoute) -> str:
        return f"{route.tags[0]}-{route.name}"
    register_models()
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        #generate_unique_id_function=custom_generate_unique_id,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app
