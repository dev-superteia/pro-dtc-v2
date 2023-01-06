from typing import Any, Optional
from sqlalchemy import select
from app.db.models.md_plant import MdPlant
from app.db.schemas import Plant
from sqlalchemy.ext.asyncio import AsyncSession


class MDplantRepository():
    async def get(db: AsyncSession) -> Optional[Plant]:
        stmt = select(MdPlant).offset(0).limit(100)
        result = await db.execute(stmt)
        return result.scalars().all()


permission = MDplantRepository()
