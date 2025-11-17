import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
#from sqlmodel import func, select

#from app.api.deps import CurrentUser, SessionDep
from app.svc import categories as cat_svc

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/")
def get_categories():
    return {'foo': 'bar'}

