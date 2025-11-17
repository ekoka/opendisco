from . import (
    user,
   account,
   product,
   category,
)
from .base import metadata

async def create_all(engine):
    async with engine.begin() as aconn:
        await aconn.run_sync(metadata.create_all)

async def drop_all(engine):
    async with engine.begin() as aconn:
        await aconn.run_sync(metadata.drop_all)
