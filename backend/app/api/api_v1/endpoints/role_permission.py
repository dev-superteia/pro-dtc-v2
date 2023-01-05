from http.client import HTTPException
from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas
from app.api import deps


router = APIRouter()


@router.get("/{id}", response_model=List[schemas.RolePermission])
async def get_permissions(
    db: AsyncSession = Depends(deps.get_db), *, id: str,
) -> Any:
    """
    Retrieve all available user roles.
    """
    roles = await repositories.role_permission.get_by_role_id(db=db,
                                                              role_id=id)
    return roles

@router.put("/{id}", response_model=str)
async def update_permission(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: str,
    permission_in: List[schemas.Permission]
) -> Any:
    """
    Update role permissions.
    """
    # Remove old permissions
    await repositories.role_permission.remove_role(db, role_id=id)
    # check if you still have permissions
    roles = await repositories.role_permission.get_by_role_id(db=db,
                                                              role_id=id)
    if roles:
        raise HTTPException(
            status_code=404,
            detail="Error occurred while updating permissions",
        )
    for permission in permission_in:
        role_permission = schemas.RolePermissionCreate(
            role_id=id, permission_id=permission.id)
        await repositories.role_permission.create(
            db=db, obj_in=role_permission)

    return "record updated successfully"
