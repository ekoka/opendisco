from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)

class Product:
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str] | None
    account_id = mapped_column(ForeignKey("account.id"))

    account: Mapped['Account'] = relationship(back_populates="account")

