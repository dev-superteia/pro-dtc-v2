from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
# from app.db.models.material_cost import MaterialCost
from app.db.schemas import RawMaterialAndCompound
from sqlalchemy.ext.asyncio import AsyncSession
import re

class MaterialEspecStdRepository():
    async def productExplode(db: AsyncSession, plant, product, month, year, type, market_segment, line):
        filter_plant = f"""and mestd.plant = '{plant}'""" if plant else ''
        filter_product = f"""and mestd.material = '{product}'""" if product else ''
        join_market = f"""left join md_material mm on mestd.material = mm.material""" if market_segment or line else ''
        filter_market = f"""and mm.mkg_segm = '{market_segment}'""" if market_segment else ''
        join_line = f"""left join market_segment ms on mm.mkg_segm = ms.mkg_segm""" if line else ''
        filter_line = f"""and ms.line = '{line}'""" if line else ''

        query = f"""
            with componentes as (select
                    mestd.plant,
                    mestd.tm_material as material ,
                    mestd.year,
                    mestd.weight,                    
                    (case when tm_material like 'ST%' or tm_material like 'YT%' then (select (mestd.weight * mest.comp_weight) as comp_weight
                    from material_espec_std_tm mest where mest.year = mestd.year and mest.plant = mestd.plant and  mest.material = mestd.tm_material
                    ) else 0 end) as comp_weigh,
                     (case when tm_material like 'ST%' or tm_material like 'YT%' then (select comp_material as comp_weight
                    from material_espec_std_tm mest where mest.year = mestd.year and mest.plant = mestd.plant and  mest.material = mestd.tm_material
                    ) else '' end) as comp_material
                from
                    material_espec_std mestd
                    {join_market}
                    {join_line}
                where
                    mestd.year = {year}
                    {filter_plant}
                    {filter_product}
                    {filter_market}
                    {filter_line}
                    and mestd.tm_material not like 'CQ%'
                    and mestd.tm_material not like 'CW%'
                    and mestd.tm_material not like '%0011'
                    and mestd.tm_material not like '%0012'
                    and mestd.material is not null),
            materials as (select plant, raw_material, raw_weight, 'KG' as measure_unit,
                    cost_std as costperunitstandard,
                    cost_std as costperuniteffective,
                    cost_std * raw_weight as totalcoststandard,
                    cost_std * raw_weight as totalcosteffective, type, concat(raw_materials.material,',',type) as material,
                    concat(raw_materials.material,';',raw_weight,';',cost_std * raw_weight,';',cost_std * raw_weight) as tm_composition
                    from
                (select
                     mesm.plant,
                     mesm.material,
                     mesm.raw_material,
                     case when mesm.raw_material like 'RG%' then 0 else mesm.raw_weight * componentes.weight end raw_weight,
                     cost_std,
                     '1' as type
                    from componentes
                    join material_espec_std_me mesm on
                        mesm.material = componentes.material and
                        mesm.plant = componentes.plant and
                        mesm.year = componentes.year
                    join material_cost mc on mc.material = raw_material and mc.year = mesm.year
                union
                select
                    mest.plant,
                    mest.material,
                    mest.raw_material,
                    case when mest.raw_material like 'RG%' then 0 else mest.raw_weight * componentes.weight end raw_weight,
                    cost_std,
                    '2' as type
                    from componentes
                    join material_espec_std_tm mest on
                        mest.material = componentes.material and
                        mest.plant = componentes.plant and
                        mest.year = componentes.year
                    join material_cost mc on mc.material = raw_material and mc.year = mest.year
                union
                select
                     componentes.plant,
                     componentes.material,
                     componentes.material as raw_material,
                     componentes.weight as raw_weight,
                     cost_std,
                     '0' as type
                    from componentes
                    join material_cost mc on mc.material = componentes.material and mc.year = componentes.year
                    where
                        componentes.material like 'RC%'
                   union 
                 select
                     mesm.plant,
                     mesm.material,
                     mesm.raw_material,
                     case when mesm.raw_material like 'RG%' then 0 else mesm.raw_weight * componentes.weight end raw_weight,
                     cost_std,
                     '4' as type
                    from componentes
                    join material_espec_std_me mesm on
                        mesm.material = componentes.comp_material and
                        mesm.plant = componentes.plant and
                        mesm.year = componentes.year
                    join material_cost mc on mc.material = raw_material and mc.year = mesm.year          
                ) raw_materials)
            select raw_material as material, max(measure_unit) as unit, max(costperunitstandard) as costperunitstandard,
                    max(costperuniteffective) as costperuniteffective, sum(raw_weight) as rawweight,
                    sum(totalcoststandard) as totalcoststandard, sum(totalcosteffective) as totalcosteffective,
                    count(distinct(material)) as totaltm, array_agg(distinct(material)) as materials, array_agg(distinct(tm_composition)) as tm_composition
                    from materials group by raw_material
                    
        """
        print(query, 'JTaa')
        sqlQuery = text(query)
        resultQuery = await db.execute(sqlQuery)
        result = list(resultQuery)
        return result


    async def listMaterialRecipesByMonth(db: AsyncSession, plant, product, year, market_segment, line):
        mes_plant = ''
        mez_plant = ''
        mkg_segm = ''
        mes_material = ''
        mez_material = ''
        line_join = ''
        line_filter = ''

        if plant:
            mes_plant = f"and mes.plant = '{plant}'"
            mez_plant = f"and mez.plant = '{plant}'"
        if product:
            mes_material = f"and mes.material = '{product}'"
            mez_material = f"and mez.material = '{product}'"
        if market_segment:
            mkg_segm = f"and mm.mkg_segm = '{market_segment}'"
        if line:
            line_join = f"left join market_segment ms on mm.mkg_segm = ms.mkg_segm"
            line_filter = f"and ms.line = '{line}'"

        query = f"""
            with totalcoststandard as (
                select distinct mes.tm_material, mes.plant,
                       (case when mes.tm_material like 'C%' then (select
                                                            sum(mc.cost_std * mesm.raw_weight)/sum(mesm.raw_weight) as preco
                                                                from
                                                                    material_espec_std_me mesm
                                                                inner join material_cost mc
                                                                    on mesm.raw_material = mc.material
                                                                where
                                                                    mesm.raw_material not like 'RG%'
                                                                    and mesm.plant = mes.plant
                                                                    and mesm.material = mes.tm_material
                                                                    and mesm.year = {year})
                            when mes.tm_material like 'S%' or mes.tm_material like 'Y%' then (
                                                               select cost_std * raw_weight as custo
                                                            from
                                                                material_espec_std_tm
                                                            inner join material_cost on
                                                                material_espec_std_tm.material = mes.tm_material
                                                                and material_espec_std_tm.raw_material = material_cost.material
                                                            where
                                                                material_espec_std_tm.plant = mes.plant
                                                                and material_espec_std_tm.material = mes.tm_material
                                                                and material_espec_std_tm.year = {year})
                         when mes.tm_material like 'RC%' then ( 
                                    select
                                        sum(mc.cost_std) as total
                                    from
                                        material_cost as mc
                                    where
                                        mc.material = mes.tm_material
                                        and mc.year = {year})
                        end) cost_std
                    from
                        material_espec_std mes
                    left join md_material mm on mes.material = mm.material
                    {line_join}
                    where
                        mes.tm_material not like 'CQ%'
                        and mes.tm_material not like 'CW%'
                        and mes.tm_material not like '%0011'
                        and mes.tm_material not like '%0012'
                        {line_filter}
                        {mes_plant}
                        {mkg_segm}
                        {mes_material}
            ),
            totalcoststdeffective as (
                select distinct mez.component, mez.plant, mez.year, mez.month,
                (case when mez.component like 'C%' then (select
                                                            sum(mc.cost_std * mez45.qtd_without)/sum(mez45.qtd_without) as preco
                                                                from
                                                                    material_espec_zp45 mez45
                                                                inner join material_cost mc
                                                                    on mc.material = mez45.component
                                                                where
                                                                    mez45.component not like 'RG%'
                                                                    and mez45.subclass in ('MPMP')
                                                                    and mez45.plant = mez.plant
                                                                    and mez45.material = mez.component
                                                                    and mez45.month = mez.month
                                                                    and mez45.qtd_without != 0
                                                                    and mez45.year = {year})
                        when mez.component like 'STM%' or mez.component like 'YTM%' then (
                            select (cost_std * mp_weight)/1000 as custo from material_espec_zp78
                                inner join material_cost on material_espec_zp78.mat_mp = material_cost.material
                                where material_espec_zp78.material = mez.component limit 1
                        )
                        when mez.component like 'STT%' or mez.component like 'YTT%' then (
                             select (cost_std * mp_weight)/1000 as custo from material_espec_zp58
                                inner join material_cost on material_espec_zp58.componente = material_cost.material
                                where material_espec_zp58.material = mez.component limit 1
                        )
                        when mez.component like 'RC%' then (
                                select
                                    sum(mc.cost_std) as total
                                from
                                    material_cost as mc
                                where
                                    mc.material = mez.component
                                    and mc.year = {year}
                        )
                    end
                    ) cost_std
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
            ),
            totalcostseffective as (
                select distinct mez.component, mez.plant, mez.year, mez.month,
                (case when mez.component like 'C%' then (select
                                                            case when mez.month = '1' then sum(mc.cost_m01 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '2' then sum(mc.cost_m02 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '3' then sum(mc.cost_m03 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '4' then sum(mc.cost_m04 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '5' then sum(mc.cost_m05 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '6' then sum(mc.cost_m06 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '7' then sum(mc.cost_m07 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '8' then sum(mc.cost_m08 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '9' then sum(mc.cost_m09 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '10' then sum(mc.cost_m10 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '11' then sum(mc.cost_m11 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                                when mez.month = '12' then sum(mc.cost_m12 * mez45.qtd_without)/sum(mez45.qtd_without)
                                                            end preco
                                                        from
                                                            material_espec_zp45 mez45
                                                        inner join material_cost mc
                                                            on mc.material = mez45.component
                                                        where
                                                            mez45.component not like 'RG%'
                                                            and mez45.subclass in ('MPMP')
                                                            and mez45.plant = mez.plant
                                                            and mez45.material = mez.component
                                                            and mez45.month = mez.month
                                                            and mez45.qtd_without != 0
                                                            and mez45.year = {year})
                        when mez.component like 'STM%' or mez.component like 'YTM%' then (
                            select
                                case when mez.month = '1' then (cost_m01 * mp_weight)/1000
                                     when mez.month = '2' then (cost_m02 * mp_weight)/1000
                                     when mez.month = '3' then (cost_m03 * mp_weight)/1000
                                     when mez.month = '4' then (cost_m04 * mp_weight)/1000
                                     when mez.month = '5' then (cost_m05 * mp_weight)/1000
                                     when mez.month = '6' then (cost_m06 * mp_weight)/1000
                                     when mez.month = '7' then (cost_m07 * mp_weight)/1000
                                     when mez.month = '8' then (cost_m08 * mp_weight)/1000
                                     when mez.month = '9' then (cost_m09 * mp_weight)/1000
                                     when mez.month = '10' then (cost_m10 * mp_weight)/1000
                                     when mez.month = '11' then (cost_m11 * mp_weight)/1000
                                     when mez.month = '12' then (cost_m12 * mp_weight)/1000
                                    end
                            from material_espec_zp78
                                inner join material_cost on material_espec_zp78.mat_mp = material_cost.material
                                where material_espec_zp78.material = mez.component limit 1
                        )
                        when mez.component like 'STT%' or mez.component like 'YTT%' then (
                             select
                                     case when mez.month = '1' then (cost_m01 * mp_weight)/1000
                                     when mez.month = '2' then (cost_m02 * mp_weight)/1000
                                     when mez.month = '3' then (cost_m03 * mp_weight)/1000
                                     when mez.month = '4' then (cost_m04 * mp_weight)/1000
                                     when mez.month = '5' then (cost_m05 * mp_weight)/1000
                                     when mez.month = '6' then (cost_m06 * mp_weight)/1000
                                     when mez.month = '7' then (cost_m07 * mp_weight)/1000
                                     when mez.month = '8' then (cost_m08 * mp_weight)/1000
                                     when mez.month = '9' then (cost_m09 * mp_weight)/1000
                                     when mez.month = '10' then (cost_m10 * mp_weight)/1000
                                     when mez.month = '11' then (cost_m11 * mp_weight)/1000
                                     when mez.month = '12' then (cost_m12 * mp_weight)/1000
                                end
                             from material_espec_zp58
                                inner join material_cost on material_espec_zp58.componente = material_cost.material
                                where material_espec_zp58.material = mez.component limit 1
                        )
                        when mez.component like 'RC%' then (
                                select
                                     case when mez.month = '1' then sum(mc.cost_m01)
                                     when mez.month = '2' then sum(mc.cost_m02)
                                     when mez.month = '3' then sum(mc.cost_m03)
                                     when mez.month = '4' then sum(mc.cost_m04)
                                     when mez.month = '5' then sum(mc.cost_m05)
                                     when mez.month = '6' then sum(mc.cost_m06)
                                     when mez.month = '7' then sum(mc.cost_m07)
                                     when mez.month = '8' then sum(mc.cost_m08)
                                     when mez.month = '9' then sum(mc.cost_m09)
                                     when mez.month = '10' then sum(mc.cost_m10)
                                     when mez.month = '11' then sum(mc.cost_m11)
                                     when mez.month = '12' then sum(mc.cost_m12)
                                    end total
                                from
                                    material_cost as mc
                                where
                                    mc.material = mez.component
                                    and mc.year = {year}
                        )
                    else 0 end) as cost_eff
                from
                    material_espec_zp45 mez
                left join md_material mm on mez.material = mm.material
                {line_join}
                where
                    mez.component not like 'CQ%'
                    and mez.component not like 'CW%'
                    and mez.component not like '%0011'
                    and mez.component not like '%0012'
                    and mez.year = {year}
                    {line_filter}
                    {mez_plant}
                    {mkg_segm}
                    {mez_material}
                    and mez.material not like 'C%' and mez.material not like 'S%' and mez.material not like 'Y%'
            ),
            volums as (
                select sum(mv.total_volum) as volum, mv.material, mv.month, mv.plant, mv.year from material_volum mv
                join (
                    select distinct mez.material
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
                ) as products on products.material = mv.material group by mv.material, mv.month, mv.year, mv.plant
            ),
            aux_materials as (
                select
                    mes.tm_material as material,
                    mes.material as product,
                    mes.plant as plant,
                    mm.mkg_segm,
                    'std' as month,
                    weight as amount_used_std,
                    weight as amount_used_eff,
                    tcs.cost_std as totalcoststd,
                    tcs.cost_std as totalcosteff,
                    (case when mes.tm_material like 'C%' then weight
                          when mes.tm_material like 'S%' or mes.tm_material like 'Y%' then weight *
                                                                                           (select coalesce(tm.raw_weight, 0)
                                                                                              from material_espec_std_tm tm where tm.material = mes.tm_material
                                                                                                and tm.plant = mes.plant and tm.year = {year})
                          when mes.tm_material like 'RC%' then weight
                     end) as amount_in_tire_kg,
                     weight * tcs.cost_std as material_cost_1_tire_standard,
                     weight * tcs.cost_std as material_cost_1_tire_effective,
                     0 as volum
                from material_espec_std mes
                    left join md_material mm on mes.material = mm.material
                    {line_join}
                    left join totalcoststandard tcs on tcs.tm_material = mes.tm_material and tcs.plant = mes.plant
                where
                    mes.tm_material not like 'CQ%'
                    and mes.tm_material not like 'CW%'
                    and mes.tm_material not like '%0011'
                    and mes.tm_material not like '%0012'
                    {line_filter}
                    {mes_plant}
                    {mkg_segm}
                    {mes_material}
                union
                select
                    mez.component as material,
                    mez.material as product,
                    mez.plant as plant,
                    mm.mkg_segm,
                    mez.month::text as month,
                    mez.utilization as amount_used_std,
                    mez.utilization as amount_used_eff,
                    tcs.cost_std as totalcoststd,
                    tce.cost_eff as totalcosteff,
                    (case when mez.component like 'C%' then mez.utilization
                          when mez.component like 'STT%' or mez.component like 'YTT%' then mez.utilization *
                                                                                           (select coalesce(mp_weight, 0)/1000
                                                                                              from material_espec_zp58 mezp58 where mezp58.material = mez.component
                                                                                                and mezp58.plant = mez.plant and mezp58.year = {year} and mezp58.month = mez.month)
                          when mez.component like 'STM%' or mez.component like 'YTM%' then mez.utilization *
                                                                                           (select coalesce(mp_weight, 0)
                                                                                              from material_espec_zp78 mezp78 where mezp78.material = mez.component
                                                                                                and mezp78.plant = mez.plant and mezp78.year = {year} and mezp78.month = mez.month)
                          when mez.component like 'RC%' then mez.utilization
                     end) as amount_in_tire_kg,
                     mez.utilization * tcs.cost_std as material_cost_1_tire_standard,
                     mez.utilization * tce.cost_eff as material_cost_1_tire_effective,
                    v.volum
                    from
                    material_espec_zp45 mez
                left join md_material mm on mez.material = mm.material
                {line_join}
                left join volums v on v.material = mez.material and v.plant = mez.plant and v.month = mez.month and v.year = mez.year
                left join totalcoststdeffective tcs on tcs.component = mez.component and tcs.plant = mez.plant and tcs.year = mez.year and tcs.month = mez.month
                left join totalcostseffective tce on tce.component = mez.component and tce.plant = mez.plant and tce.year = mez.year and tce.month = mez.month
                where
                    mez.component not like 'CQ%'
                    and mez.component not like 'CW%'
                    and mez.component not like '%0011'
                    and mez.component not like '%0012'
                    and mez.material not like 'C%' and mez.material not like 'S%' and mez.material not like 'Y%'
                    and mez.year = {year}
                    {line_filter}
                    {mez_plant}
                    {mkg_segm}
                    {mez_material}
            ),
            materials as (
            select material.material, material.month, material.amount_used_std,  material.amount_used_eff,
                   material.totalcoststd, material.totalcosteff,  material.amount_in_tire_kg,
                   material.material_cost_1_tire_standard,
                   material.material_cost_1_tire_effective,
                   material.amount_used_std * material.volum amount_used_std_volum, material.amount_used_eff*material.volum amount_used_eff_volum,
                   material.totalcoststd * material.volum totalcoststd_volum, material.totalcosteff * material.volum totalcosteff_volum,
                   material.amount_in_tire_kg * material.volum amount_in_tire_kg_volum,
                   material.material_cost_1_tire_standard * material.volum material_cost_1_tire_standard_volum,
                   material.material_cost_1_tire_effective * material.volum material_cost_1_tire_effective_volum,
                   Coalesce((aux.material_cost_1_tire_standard - material.material_cost_1_tire_standard),(0-material.material_cost_1_tire_standard)) as dtc,
                   (aux.material_cost_1_tire_standard - material.material_cost_1_tire_standard) * material.volum as dtc_volum
            from aux_materials material
                            left join aux_materials aux on material.product = aux.product and material.plant = aux.plant and material.material = aux.material and aux.month = 'std')
            select material, month, sum(amount_used_std) amount_used_std, sum(amount_used_eff) amount_used_eff,
                   sum(totalcoststd) totalcoststd, sum(totalcosteff) totalcosteff, sum(amount_in_tire_kg) amount_in_tire_kg,
                   sum(material_cost_1_tire_standard) material_cost_1_tire_standard,
                   sum(material_cost_1_tire_effective) material_cost_1_tire_effective,
                   case when month = 'std' then 0 else Coalesce(sum(dtc),0) end dtc,
                   sum(amount_used_std_volum) amount_used_std_volum, sum(amount_used_eff_volum) amount_used_eff_volum,
                   sum(totalcoststd_volum) totalcoststd_volum, sum(totalcosteff_volum) totalcosteff_volum,
                   sum(amount_in_tire_kg_volum) amount_in_tire_kg_volum,
                   sum(material_cost_1_tire_standard_volum) material_cost_1_tire_standard_volum,
                   sum(material_cost_1_tire_effective_volum) material_cost_1_tire_effective_volum,
                   case when month = 'std' then 0 else sum(dtc_volum) end dtc_volum
                   from materials group by material, month;
        """

        sqlQuery = text(query)
        print(sqlQuery)
        resultQuery = await db.execute(sqlQuery)
        result = list(resultQuery)
        return result


    async def find_name_tissue(db: AsyncSession, plant, material, tm_material, type, year):
        if type == 'std':
            sqlQuery = text("""
            select
               raw_material
            from
                material_espec_std_tm
            where
                material_espec_std_tm.material = '""" + tm_material + """' limit 1
            """)
        else:
            if re.search("^(S|Y)TM.+$", tm_material):
                sqlQuery = text("""
                    select mat_mp from material_espec_zp78
                    where material_espec_zp78.material = '""" + tm_material + """' limit 1
                """)
            else:
                sqlQuery = text("""
                    select componente from material_espec_zp58
                    where material_espec_zp58.material = '""" + tm_material + """' limit 1
                """)

        result = await db.execute(sqlQuery)
        cost = [row[0] for row in result]
        if len(cost) <= 0 or cost[0] is None:
            return ' '
        return cost[0]