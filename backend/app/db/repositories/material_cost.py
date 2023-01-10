from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
from app.db.models.material_cost import MarketCost
from app.db.schemas import PlantInDBBase
from sqlalchemy.ext.asyncio import AsyncSession

class MaterialCostRepository():
    async def is_cost_null(db: AsyncSession, plant, year) -> Optional[PlantInDBBase]:
        filter_plant = f"""and mez.plant = '{plant}'""" if plant else ''  
        query = f"""select distinct mez.component, mez.plant, mez.year         
          from
             material_espec_zp45 mez left join material_cost mc on mc.material = mez.component       
           where
               mez.subclass = 'MPMP' and mc.cost_std is null {filter_plant} and mez.year = '{year}' group by mez.component,mez.plant, mez.year"""
        sqlQuery = text(query)
        resultQuery = await db.execute(sqlQuery)
        result = list(resultQuery)
        return result