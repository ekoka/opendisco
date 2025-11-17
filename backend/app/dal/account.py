from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)

from .base import Base

class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    name: Mapped[str] | None
    description: Mapped[str] | None

    #products: Mapped[list["Product"]] = relationship(back_populates="account")

