import functools
from sqlalchemy import MetaData
from sqlalchemy.orm import registry

from .user import User
from .account import Account
from .product import Product

@functools.cache
def get_metadata():
    return MetaData()

@functools.cache
def get_registry():
    return registry(metadata=get_metadata())

def register_models():
    """
    Import and register models explicitly. I prefer this approach. Implicit model registration
    (via declarative base) does not avoid still needing to discover models later. Except that
    in the latter case, it'll likely be through an empty import whose sole purpose is its 
    discovery side-effect.
    """
    reg = get_registry()
    reg.mapped_as_dataclass(User)
    reg.mapped_as_dataclass(Account)
    reg.mapped_as_dataclass(Product)
