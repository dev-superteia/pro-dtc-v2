from typing import Optional
from pydantic import UUID4, BaseModel


# Shared properties
class PermissionBase(BaseModel):
    name: Optional[str]
    description: Optional[str]


# Properties to receive via API on creation
class PermissionCreate(PermissionBase):
    pass


# Properties to receive via API on update
class PermissionUpdate(PermissionBase):
    name: Optional[str]
    description: Optional[str]


class PermissionInDBBase(PermissionBase):
    id: UUID4

    class Config:
        orm_mode = True


# Additional properties to return via API
class Permission(PermissionInDBBase):
    pass


class PermissionInDB(PermissionInDBBase):
    pass
