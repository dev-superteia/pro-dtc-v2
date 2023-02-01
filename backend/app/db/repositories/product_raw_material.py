from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
# from app.db.models.material_cost import MaterialCost
from app.db.schemas import RawMaterialAndCompound
from sqlalchemy.ext.asyncio import AsyncSession

class ProductRawMaterialRepository():
    async def productExplodeZp45(db: AsyncSession, plant, product, month, year, type, market_segment, line):
        filter_plant = f"""and mez.plant = '{plant}'""" if plant else ''
        filter_product = f"""and mez.material = '{product}'""" if product else ''
        join_market = f"""left join md_material mm on mez.material = mm.material""" if market_segment or line else ''
        filter_market = f"""and mm.mkg_segm = '{market_segment}'""" if market_segment else ''
        join_line = f"""left join market_segment ms on mm.mkg_segm = ms.mkg_segm""" if line else ''
        filter_line = f"""and ms.line = '{line}'""" if line else ''

        query = f"""
            with componentes_aux as (
                select
                    mez.plant,
                    mez.component,
                    mez.measure_unit,
                    mez.utilization,
                    mez.month,
                    mez.year,
                    mez.material as product,
                    sum(mv.total_volum) as volum
                from
                    material_espec_zp45 mez
                    {join_market}
                    {join_line}
                    left join material_volum mv on mez.material = mv.material and mv.plant = mez.plant and mv.month = mez.month and mv.year = mez.year
                    where
                        mez.year = {year}
                        {filter_plant}
                        {filter_product}
                        and mez.month = '{month}'
                        {filter_market}
                        {filter_line}
                        and mez.material not like 'C%' and mez.material not like 'S%' and mez.material not like 'Y%'
                        group by mez.material, mez.plant, mez.measure_unit, mez.utilization, mez.component, mez.month, mez.year
                        ),
             componentes as (select * , 
                    (case when comp.component like 'STT%' or comp.component like 'YTT%' then (select (mez.mp_weight * utilization) as comp_weight
                    from material_espec_zp58 mez where comp.component = mez.material and comp."month" = mez."month" and comp.plant  = mez.plant and comp."year" = mez."year"                 
                    ) when comp.component like 'STM%' or comp.component like 'YTM%' then (select (mez78.mp_weight * utilization) as comp_weight
                    from material_espec_zp78 mez78 where comp.component = mez78.material and comp."month" = mez78."month" and comp.plant  = mez78.plant and comp."year" = mez78."year"                 
                    )else 0 end)as comp_weight,
                    (case when comp.component like 'STT%' or comp.component like 'YTT%' then (select mez.mat_me
                    from material_espec_zp58 mez where comp.component = mez.material and comp."month" = mez."month" and comp.plant  = mez.plant and comp."year" = mez."year"                 
                    ) when comp.component like 'STM%' or comp.component like 'YTM%' then (select mez78.mat_me
                    from material_espec_zp78 mez78 where comp.component = mez78.material and comp."month" = mez78."month" and comp.plant  = mez78.plant and comp."year" = mez78."year"                 
                    )else '' end) as comp_me from componentes_aux comp),            
            aux_materials as (
                select concat(raw_materials.material,',',type) as material, 
                       raw_materials.material as material_name,
                       raw_material, case when raw_material like 'RG%' then 0 else raw_weight end raw_weight,
                       mc.cost_std as costperunitstandard,
                       case when month = '01' then mc.cost_m01
                            when month = '02' then mc.cost_m02
                            when month = '03' then mc.cost_m03
                            when month = '04' then mc.cost_m04
                            when month = '05' then mc.cost_m05
                            when month = '06' then mc.cost_m06
                            when month = '07' then mc.cost_m07
                            when month = '08' then mc.cost_m08
                            when month = '09' then mc.cost_m09
                            when month = '10' then mc.cost_m10
                            when month = '11' then mc.cost_m11
                            when month = '12' then mc.cost_m12
                    end costperuniteffective, type, volum
                from
                    (select componentes.plant,
                        componentes.component as material,
                        mez2.component as raw_material,
                        (case when mez2.qtd_without = 0 then mez2.utilization else mez2.qtd_without end) * componentes.utilization as raw_weight,
                        mez2.month,
                        componentes.year,
                        '1' as type,
                        volum
                        from componentes
                        inner join material_espec_zp45 mez2 on
                            componentes.component = mez2.material
                            and componentes.plant = mez2.plant
                            and componentes.year = mez2.year
                            and componentes.month = mez2.month
                    union
                    select componentes.plant,
                        componentes.component as material,
                        mez2.component as raw_material,
                        (case when mez2.qtd_without = 0 then mez2.utilization else mez2.qtd_without end) * componentes.comp_weight as raw_weight,
                        mez2.month,
                        componentes.year,
                        '4' as type,
                        volum
                        from componentes
                        inner join material_espec_zp45 mez2 on
                            componentes.comp_me  = mez2.material
                            and componentes.plant = mez2.plant
                            and componentes.year = mez2.year
                            and componentes.month = mez2.month
                    union
                    select componentes.plant,
                        componentes.component,
                        componentes.component,
                        componentes.utilization as raw_weight,
                        componentes.month,
                        componentes.year,
                        '0' as type,
                        volum
                        from componentes
                        where
                        componentes.component like 'RC%'
                    union
                    select
                        componentes.plant,
                        mezp58.componente,
                        (select
                            raw_material
                        from
                            material_espec_std_tm
                        where
                            material_espec_std_tm.material = componentes.component
                            and material_espec_std_tm.plant = componentes.plant limit 1),
                        mezp58.mp_weight/1000 * componentes.utilization as raw_weight,
                        mezp58.month,
                        componentes.year,
                        '2' as type,
                        volum
                        from componentes
                        inner join material_espec_zp58 mezp58 on
                            componentes.component = mezp58.material
                            and componentes.plant = mezp58.plant
                            and componentes.year = mezp58.year
                            and componentes.month = mezp58.month
                        where componentes.component like 'STT%' or componentes.component like 'YTT%'
                    union
                    select
                        componentes.plant,
                        componentes.component,
                        (select
                            raw_material
                        from
                            material_espec_std_tm
                        where
                            material_espec_std_tm.material = componentes.component
                            and material_espec_std_tm.plant = componentes.plant limit 1),
                        mezp78.mp_weight/1000 * componentes.utilization as raw_weight,
                        mezp78.month,
                        componentes.year,
                        '2' as type,
                        volum
                        from componentes
                        inner join material_espec_zp78 mezp78 on
                            componentes.component = mezp78.material
                            and componentes.plant = mezp78.plant
                            and componentes.year = mezp78.year
                            and componentes.month = mezp78.month
                        where componentes.component like 'STM%' or componentes.component like 'YTM%'
                    ) raw_materials join material_cost mc on mc.material = raw_material and mc.year = raw_materials.year),
            materials as (select *, 
            raw_weight * costperunitstandard as totalcoststandard, 
            raw_weight * costperuniteffective as totalcosteffective,
            raw_weight * volum as raw_weight_volum,
            costperunitstandard * volum as costperunitstandard_volum,
            costperuniteffective * volum as costperuniteffective_volum,
            raw_weight * costperunitstandard * volum as totalcoststandard_volum,
            raw_weight * costperuniteffective * volum as totalcosteffective_volum,
            concat(material_name, ';', raw_weight, ';', raw_weight * costperunitstandard, ';', raw_weight * costperuniteffective,
                   ';', raw_weight * volum, ';', raw_weight * costperunitstandard * volum, ';', raw_weight * costperuniteffective * volum) as tm_composition
            from aux_materials)
            select raw_material as material, 'KG' as unit, max(costperunitstandard) as costperunitstandard,
                   max(costperuniteffective) as costperuniteffective, sum(raw_weight) as rawweight,
                   sum(totalcoststandard) as totalcoststandard, sum(totalcosteffective) as totalcosteffective,
                   max(costperunitstandard_volum) as costperunitstandard_volum,
                   max(costperuniteffective_volum) as costperuniteffective_volum, sum(raw_weight_volum) as raw_weight_volum,
                   sum(totalcoststandard_volum) as totalcoststandard_volum, sum(totalcosteffective_volum) as totalcosteffective_volum,
                   count(distinct(material)) as totaltm, array_agg(distinct(material)) as materials, array_agg(distinct(tm_composition)) as tm_composition
                   from materials group by raw_material;
        """

        sqlQuery = text(query)
        resultQuery = await db.execute(sqlQuery)
        result = list(resultQuery)
        return result