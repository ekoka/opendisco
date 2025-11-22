import asyncio
import uuid
from typing import Any, Callable

from fastapi import APIRouter, HTTPException

from app.svc import errors as svc_err
from app.svc import users as usr_svc
from app.svc import email as eml_svc
from app.val.users import UserCreate
#from app.api.deps import CurrentUser
from app.api.deps.db import SessionDep


from app.val.users import (
    UserCreate,
    UserPublic,
    UserRegister,
    UsersPublic,
    UserUpdate,
    ProfileUpdate,
)

router = APIRouter(prefix="/users", tags=["Users"])

async def run_or_raise(task, status_code: int = 400, detail: str = "Malformed data"):
    try:
        return await task
    except svc_err.ServiceError as e:
        raise HTTPException(
            status_code=e.status_code if e.status_code else status_code,
            detail=e.detail if e.detail else detail,
        )
    except:
        raise
        # TODO: Log error
        raise HTTPException(
            status_code=500,
            detail="An error occurred in the system",
        )

@router.get("/")
def get_users():
    return {'foo': 'bar'}

def task(cb, *a, **kw): 
    return asyncio.create_task(cb(*a, **kw))

@router.post("/", response_model=UserPublic)
async def post_user(*, Session: SessionDep, user_in: UserCreate) -> Any:
    user_id = await run_or_raise(task(usr_svc.create_user, Session, user_in))
    #if settings.emails_enabled and user_in.email:
    #    email_data = generate_new_account_email(
    #        email_to=user_in.email, username=user_in.email, password=user_in.password
    #    )
    #    eml_svc.send_email(
    #        email_to=user_in.email,
    #        subject=email_data.subject,
    #        html_content=email_data.html_content,
    #    )
    return UserPublic(id=user_id)

#@router.post(
#    "/", dependencies=[Depends(get_current_active_superuser)], response_model=UserPublic
#)
#def post_user(*, session: SessionDep, user_in: UserCreate) -> Any:
#    user = crud.get_user_by_email(session=session, email=user_in.email)
#    if user:
#        raise HTTPException(
#            status_code=400,
#            detail="The user with this email already exists in the system.",
#        )
#
#    user = crud.create_user(session=session, user_create=user_in)
#    if settings.emails_enabled and user_in.email:
#        email_data = generate_new_account_email(
#            email_to=user_in.email, username=user_in.email, password=user_in.password
#        )
#        send_email(
#            email_to=user_in.email,
#            subject=email_data.subject,
#            html_content=email_data.html_content,
#        )
#    return user
