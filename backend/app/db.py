from sqlalchemy import create_engine

from app.settings import settings 

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=settings.SQLALCHEMY_ECHO,
)

