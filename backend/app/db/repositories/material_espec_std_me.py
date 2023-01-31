from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import MaterialEspecStdMe

class MaterialEspecStdMeRepository:
    
    async def explode_material(db: AsyncSession, plant, tm_material, year):
        stmt = select(MaterialEspecStdMe).filter(MaterialEspecStdMe.plant == plant, MaterialEspecStdMe.material == tm_material, MaterialEspecStdMe.year == year)
        result = await db.execute(stmt)
        result = result.scalars()
        return result