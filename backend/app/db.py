import functools
from typing import TypeAlias, Callable


from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

from app.settings import settings 
from app.dal.base import Base 

@functools.cache
def get_engine() -> AsyncEngine:
    return create_async_engine(
        settings.SQLALCHEMY_DATABASE_URI,
        echo=settings.SQLALCHEMY_ECHO,
    )

Session = functools.partial(AsyncSession, get_engine())
# Use this as the type for Session 
SessionFactory: TypeAlias = Callable[[], AsyncSession]
