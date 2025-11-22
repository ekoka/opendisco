from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy

from .base import Base

class CommonWord(Base):
    """
    This model can be useful to prevent some easily guessable passwords.
    """
    __tablename__ = 'common_word'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    word: Mapped[str]


class ReservedWord(db.Model):
    """
    This model can be used to prevent subdomain registration with potentially
    problematic words.
    """
    __tablename__ = 'reserved_word'
    
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    word: Mapped[str]

