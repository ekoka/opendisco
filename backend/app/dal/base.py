from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

class Base(MappedAsDataclass, DeclarativeBase): 
    def __call__(self, **data):
        for k,v in data.items():
            if hasattr(self, k):
                setattr(self, k, v)

metadata = Base.metadata

