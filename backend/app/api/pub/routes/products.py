import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
#from sqlmodel import func, select

#from app.api.deps import CurrentUser, SessionDep
#from app.dal import Item, ItemCreate, ItemPublic, ItemsPublic, ItemUpdate, Message

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def get_products():
    return {'foo': 'bar'}

