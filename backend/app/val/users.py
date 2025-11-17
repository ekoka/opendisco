from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    fullname: str

class UserPublic(BaseModel): pass
class UserRegister(BaseModel): pass
class UsersPublic(BaseModel): pass
class UserUpdate(BaseModel): pass
class ProfileUpdate(BaseModel): pass
