from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
# from app.db.models.material_cost import MaterialCost
from app.db.schemas import RawMaterialAndCompound
from sqlalchemy.ext.asyncio import AsyncSession

class RawMaterialAndCompoundRepository():
    async def listComponents(db: AsyncSession, type, plant, market_segment, line, year, type_selected) -> Optional[RawMaterialAndCompound]:
        filter_plant = f"""and mez.plant = '{plant}'""" if plant else ''       
        filter_plant_raw = f"""and plant = '{plant}'""" if plant else ''
        filter_plant_comp = f"""and comp.plant = '{plant}'""" if plant else ''           
        filter_line = f"""and ms.line = '{line}'""" if line else ''
        
        
        if type == 'raw_material':  
            filter_type = f"""and mez2.component  = '{type_selected}'""" if type_selected else ''      
            query = f"""select component, array_agg(jsonb_build_array(utilization,volume,total,month))  from (select mez.component,sum(utilization) utilization, comp."month", comp.volume, sum(utilization) * comp.volume as total from  material_espec_zp45 mez inner join md_material mm on 
                        mm.material  = mez.material left join market_segment ms on mm.mkg_segm = ms.mkg_segm, 
                        (select mez2.material, mez2.component,sum(utilization) as volume, "month"
                        from material_espec_zp45 mez2 where component = '{type_selected}' {filter_plant_raw} group by mez2.material, mez2.component, "month" ) as comp where mez.component = comp.material 
                        {filter_plant} {filter_line} and mez.year = """+year+""" and mez."month" = comp.month group by mez.component, comp.component, mez."month", comp.month,comp.volume) as material
                        group by component"""

        else:
            filter_type = f"""and mez.component = '{type_selected}'""" if type_selected else ''   
            query = f"""select mx.material,mez.plant, mx.mat_desc, array_agg(jsonb_build_array(mez."month",mez.utilization,coalesce((select sum(mv.total_volum)as 
                        volume from material_volum mv where material = mx.material and  mv.plant = mez.plant and "month" = mez."month" group by material),0))), mx.line                         
                        from (select mm.material, mm.mat_desc, ms.line from md_material mm left join market_segment
                        ms on mm.mkg_segm = ms.mkg_segm where
                        mm.subclass = 'IPAA'{filter_line}) as mx, material_espec_zp45 mez where mez.material = mx.material 
                        {filter_plant} {filter_type} and mez.year = """+year+""" group by mx.material, plant, mx.line, mx.mat_desc"""
        sqlQuery = text(query)
        resultQuery = await db.execute(sqlQuery)
        result = list(resultQuery)
        return result