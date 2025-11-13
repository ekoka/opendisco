from fastapi import APIRouter

#from app.api.adm.routes import items, login, private, users, utils
from .adm.routes import account

api_router = APIRouter()
api_router.include_router(account.router)
#api_router.include_router(login.router)
#api_router.include_router(users.router)
#api_router.include_router(utils.router)


#from app.core.config import settings
#if settings.ENVIRONMENT == "local":
#    api_router.include_router(private.router)
