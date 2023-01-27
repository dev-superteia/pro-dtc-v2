from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
# from app.db.models.material_cost import MaterialCost
from app.db.schemas import RawMaterialAndCompound
from sqlalchemy.ext.asyncio import AsyncSession

class MaterialVolumRepository():
    async def list_volum_by_month(db: AsyncSession, plant, product, year, market_segment, line):
        mez_plant = ''
        mkg_segm = ''
        mez_material = ''
        line_join = ''
        line_filter = ''

        if plant:
            mez_plant = f"and mez.plant = '{plant}'"
        if product:
            mez_material = f"and mez.material = '{product}'"
        if market_segment:
            mkg_segm = f"and mm.mkg_segm = '{market_segment}'"
        if line:
            line_join = f"left join market_segment ms on mm.mkg_segm = ms.mkg_segm"
            line_filter = f"and ms.line = '{line}'"

        query = f"""select sum(mv.total_volum) as volum, sum(mv.total_value) as value, mv.month from material_volum mv
                        join (
                            select distinct mez.material, mez.plant, mez.year
                            from
                                material_espec_zp45 mez
                            left join md_material mm on mez.material = mm.material
                            {line_join}
                            where
                                mez.component not like 'CQ%'
                                and mez.component not like 'CW%'
                                and mez.component not like '%0011'
                                and mez.component not like '%0012'
                                {line_filter}
                                {mez_plant}
                                {mkg_segm}
                                {mez_material}
                                and mez.material not like 'C%' and mez.material not like 'S%' and mez.material not like 'Y%'
                                and mez.year = {year}
                        ) as products on products.material = mv.material and products.plant = mv.plant and products.year = mv.year group by mv.month
                    """
        print(query)
        sqlQuery = text(query)
        resultQuery = await db.execute(sqlQuery)
        result = list(resultQuery)
        return result