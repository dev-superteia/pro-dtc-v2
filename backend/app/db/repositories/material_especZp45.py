from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
from app.db.models.material_espec_zp45 import MaterialEspecZp45
from app.db.schemas import Plant
from sqlalchemy.ext.asyncio import AsyncSession


class MaterialEspecZp45Repository():
    async def find_material_utilization(db: AsyncSession, plant, material, component, month, year):
        stmt = select(MaterialEspecZp45).filter(MaterialEspecZp45.plant == plant,
                                                MaterialEspecZp45.material == material, 
                                                MaterialEspecZp45.component == component, 
                                                MaterialEspecZp45.month == month, 
                                                MaterialEspecZp45.year == year)
        result = await db.execute(stmt)
        result = result.scalars().first()
        if result is None:
            return 0
        return result['utilization']


    async def find_by_plant_component_month_year(db: AsyncSession, plant, component, month, year):
        stmt = select(MaterialEspecZp45).filter(MaterialEspecZp45.plant == plant,
                                                MaterialEspecZp45.material == component, 
                                                MaterialEspecZp45.month == month, 
                                                MaterialEspecZp45.year == year,
                                                MaterialEspecZp45.subclass == 'MPMP', or_(MaterialEspecZp45.component.notlike('CQ%'), MaterialEspecZp45.component.notlike('CW%')))
        result = await db.execute(stmt)
        result = result.scalars().all()
        return result
    
    
    async def find_material_measure_unit(db: AsyncSession, plant, material, component):
        stmt = select(MaterialEspecZp45).filter(MaterialEspecZp45.plant == plant,
                                                MaterialEspecZp45.material == material, 
                                                MaterialEspecZp45.component == component)
        result = await db.execute(stmt)
        result = result.scalars().all()
        if result is None:
            return ''
        return result


material_zp45 = MaterialEspecZp45Repository()
