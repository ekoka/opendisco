import asyncio
import sys

print(sys.path)

from app.dal import create_all
from app.db import get_engine

def db_create_all():
    asyncio.run(create_all(get_engine()))

if __name__=='__main__':
    db_create_all()
