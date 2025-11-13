from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)

class Account:
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] | None
    description: Mapped[str] | None

    products: Mapped[list["Product"]] = relationship(back_populates="account")

