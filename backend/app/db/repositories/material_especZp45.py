from typing import Any, Optional
from sqlalchemy import select
from app.db.models.material_espec_zp45 import MaterialEspecZp45
from app.db.schemas import Plant
from sqlalchemy.ext.asyncio import AsyncSession


class MaterialEspecZp45():
    async def find_material_utilization(db: AsyncSession, plant, material, component, month, year):
        stmt = select(MaterialEspecZp45).filter(MaterialEspecZp45.plant == plant,
                                                MaterialEspecZp45.material == material, 
                                                MaterialEspecZp45.component == component, 
                                                MaterialEspecZp45.month == month, 
                                                MaterialEspecZp45.year == year).first()
        result = await db.execute(stmt)
        result = result.scalars().first()
        if result is None:
            return 0
        return result['utilization']


material_zp45 = MaterialEspecZp45()
