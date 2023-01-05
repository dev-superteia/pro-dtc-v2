from typing import List, Optional
from pydantic import UUID4, BaseModel
from .permission import Permission


# Shared properties
class RolePermissionBase(BaseModel):
    permission_id: Optional[UUID4]
    role_id: Optional[UUID4]


# Properties to receive via API on creation
class RolePermissionCreate(RolePermissionBase):
    pass


# Properties to receive via API on update
class RolePermissionUpdate(BaseModel):
    permission_id: UUID4


class RolePermissionInDBBase(RolePermissionBase):
    permission: Optional[Permission]

    class Config:
        orm_mode = True


# Additional properties to return via API
class RolePermission(RolePermissionInDBBase):
    pass


class RolePermissionInDB(RolePermissionInDBBase):
    pass
