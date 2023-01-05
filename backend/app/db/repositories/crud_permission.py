from app.db.models.permission import Permission
from app.db.repositories.base import CRUDBase
from app.db.schemas import PermissionCreate, PermissionUpdate
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDPermission(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):
    async def create(self, db: AsyncSession, *,
                     obj_in: PermissionCreate) -> Permission:
        db_obj = Permission(
            name=obj_in.name,
            description=obj_in.description,
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


permission = CRUDPermission(Permission)
