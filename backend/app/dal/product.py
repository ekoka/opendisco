from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy

from .base import Base

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]
    description: Mapped[str] | None
    account_id = mapped_column(ForeignKey("account.id"))

    # relationships
    #account: Mapped['Account'] = relationship(back_populates="products")
    categories: Mapped[list['Category']] = relationship(
        secondary='product_category',
        back_populates='products',
    )

    # aliases
    #cats: AssociationProxy[list[str]] = association_proxy('categories', 'name')


