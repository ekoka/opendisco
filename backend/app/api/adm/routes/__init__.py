import functools

from fastapi import APIRouter

from . import accounts, users

@functools.cache
def get_routes():
    r = APIRouter(prefix="/adm")
    r.include_router(accounts.router)
    r.include_router(users.router)
    return r 
