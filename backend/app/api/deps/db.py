from typing import Annotated

from fastapi import Depends

from app.db import SessionFactory, Session

def get_session() -> SessionFactory:
    return Session

SessionDep = Annotated[SessionFactory, Depends(get_session)]
