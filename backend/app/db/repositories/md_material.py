from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
from app.db.models.md_material import MdMaterial
from app.db.schemas import Material
from sqlalchemy.ext.asyncio import AsyncSession


class MdMaterialRepository():
    async def get_tires(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(MdMaterial.subclass == 'IPAA')
        result = await db.execute(stmt)
        return result.scalars().all()
    async def all_mass(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(and_(MdMaterial.subclass != 'IPAA',MdMaterial.subclass != 'MPMP',MdMaterial.subclass != None,MdMaterial.subclass != '' ))
        result = await db.execute(stmt)
        return result.scalars().all()
    async def get_tissue(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(or_(MdMaterial.subclass == 'G1TM',MdMaterial.subclass == 'G1TT'))
        result = await db.execute(stmt)
        return result.scalars().all()
    async def get_mass(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(and_(MdMaterial.subclass != 'IPAA',MdMaterial.subclass != 'MPMP',MdMaterial.subclass != None,MdMaterial.subclass != '',MdMaterial.subclass != 'G1TM',MdMaterial.subclass != 'G1TT'))
        result = await db.execute(stmt)
        return result.scalars().all()
    async def get_raw_material(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(or_(MdMaterial.subclass == 'MPMP',MdMaterial.subclass == None,MdMaterial.subclass == ''))
        result = await db.execute(stmt)
        return result.scalars().all()
    
    async def get_raw(db: AsyncSession) -> Optional[Material]:
        query = f"""select * from md_material"""
        sqlQuery = text(query)
        resultQuery = await db.execute(sqlQuery)
        return resultQuery
    

permission = MdMaterialRepository()
