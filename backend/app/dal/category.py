from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)

class Category:
    """
    Product category
    """
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str] | None

    products: Mapped['Account'] = relationship(back_populates="account")

