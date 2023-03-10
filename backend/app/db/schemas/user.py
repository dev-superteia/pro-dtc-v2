from typing import List, Optional # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr
from app.db.schemas.user_role import UserRole


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: UUID4
    # created_at: datetime
    # updated_at: datetime
    user_role: Optional[List[UserRole]]

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class UserLogin(BaseModel):
    username: EmailStr
    password: str
