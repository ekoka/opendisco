import functools

from sqlalchemy import create_engine, Engine

from app.settings import settings 

@functools.cache
def get_engine() -> Engine:
    return create_engine(
        settings.SQLALCHEMY_DATABASE_URI,
        echo=settings.SQLALCHEMY_ECHO,
    )


