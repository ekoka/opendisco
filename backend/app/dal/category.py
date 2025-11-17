from sqlalchemy import (
    Integer, 
    ForeignKey, 
    Table,
    Column,
)
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)

from .base import Base

class Category(Base):
    """
    Product category
    """
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str] | None

    products: Mapped[list['Product']] = relationship(
        secondary="product_category", 
        back_populates='categories'
    )

product_category_tbl = Table(
    'product_category',
    Base.metadata,
    Column('product_id', Integer, ForeignKey("product.id"), primary_key=True),
    Column('category_id', Integer, ForeignKey("category.id"), primary_key=True),
)
