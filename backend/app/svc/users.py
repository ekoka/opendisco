from sqlalchemy import select, insert

from app.val.users import (
    UserCreate,
    #UserPublic,
    #UserRegister,
    #UsersPublic,
    #UserUpdate,
    #ProfileUpdate,
)
from app.dal.user import User
from app.db import SessionFactory
from app.utils import security as sec

from .errors import ServiceError

async def create_user(Session: SessionFactory, data: UserCreate): 
    email_found = await email_is_registered(Session, data.email)
    if email_found:
        raise ServiceError(
            status_code=400,
            detail="A user with this email has already been registered in the system.",
        )
    uid = None
    async with Session() as session:
        data.password = sec.hash_password(data.password)
        m = data.model_dump()
        u = User(**m)
        session.add(u)
        await session.commit()
        uid = u.id
    return uid 


async def email_is_registered(Session: SessionFactory, email: str) -> bool:
    async with Session() as session:
        res = await session.scalars(
            select(User.email).filter_by(email=email).limit(1)
        )
    return bool(res.first())
