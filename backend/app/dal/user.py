from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)

from .base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String, insert_default='basic', init=False)
    fullname: Mapped[str] | None

