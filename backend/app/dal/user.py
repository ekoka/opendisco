from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)

class User:
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    fullname: Mapped[str] | None

