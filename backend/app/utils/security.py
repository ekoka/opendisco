import datetime as dt
from typing import Any, TypeAlias, Callable
from dataclass import dataclass

import jwt
import argon2


from app.core.config import settings


from app.utils.string import unicode_normalizer

ALGORITHM = "HS256"

pw_hasher = argon2.PasswordHasher()

def create_access_token(subject: str | Any, expires_delta: dt.timedelta) -> str:
    expire = dt.datetime.now(dt.timezone.utc) + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def hash_password(plain_pw: bytes|str) -> str:
    if type(plain_pw) is str:
        plain_pw = unicode_normalizer(plain_pw)
        plain_pw = plain_pw.encode('utf-8')
    # no need to explicitly salt, done automatically.
    hashed_pw = pw_hasher.hash(plain_pw)
    return hashed_pw.decode('utf-8')

@dataclass
class LoginError(Exception):
    status_code: int
    detail: str

PasswordUpdaterCallback: TypeAlias = Callable[[str|bytes], bool]
def verify_password(
        hashed_pw str|bytes, 
        plain_pw: str|bytes,
        update_pw_cb: PasswordUpdaterCallback=None
    ) -> bool:
    if type(hashed_pw) is str:
        hashed_pw = hashed_pw.encode('utf-8')
    if type(plain_pw) is str:
        plain_pw = unicode_normalizer(plain_pw)
        plain_pw = plain_pw.encode('utf-8')

    exc = argon2.exceptions
    try:
        pw_hasher.verify(hashed_pw, password)
    except exc.VerifyMismatchError:
        raise LoginError(status_code=400, "Password mismatch")
    except (exc.VerificationError, exc.InvalidHashError) as e:
        raise e
    if pw_hasher.check_needs_rehash(hashed_pw):
        if update_pw_cb is None:
            return False
        return update_pw_cb(pw_hasher.hash(plain_pw))
    return True

