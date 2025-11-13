from sqlalchemy import MetaData
from sqlalchemy.orm import registry

from .admin import Admin
from .account import Account
from .product import Product

"""
Import and register models explicitly. I prefer this approach. Implicit model registration
(via declarative base) does not avoid still needing to discover models later. Except that
in the latter case, it'll likely be through an empty import whose sole purpose is its discovery
side-effect.
"""
metadata = MetaData()
reg = registry(metadata=metadata)
reg.mapped_as_dataclass(Admin)
reg.mapped_as_dataclass(Account)
reg.mapped_as_dataclass(Product)
