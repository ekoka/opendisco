import asyncio

from app.dal import drop_all
from app.db import get_engine

def db_drop_all():
    asyncio.run(drop_all(get_engine()))

if __name__=='__main__':
    db_drop_all()
