from typing import Any, Optional
from sqlalchemy import select, and_, or_, text
from app.db import repositories 
from app.db.schemas import Material
from sqlalchemy.ext.asyncio import AsyncSession
import re
from decimal import Decimal

from app.db.models import MaterialEspecZp45, MaterialEspecZp58, MaterialEspecZp78, MdMaterial, MaterialEspecStdTm

class MdMaterialRepository():
    async def get_tires(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(MdMaterial.subclass == 'IPAA')
        result = await db.execute(stmt)
        return result.scalars().all()

    async def all_mass(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(and_(MdMaterial.subclass != 'IPAA', MdMaterial.subclass !=
                                              'MPMP', MdMaterial.subclass != None, MdMaterial.subclass != '',MdMaterial.material.not_like(
                                                  'CQ%'),
                                              MdMaterial.material.not_like(
                                                  'CW%'), MdMaterial.material.not_like('%0011'),
                                              MdMaterial.material.not_like('%0012')))
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_tissue(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(
            or_(MdMaterial.subclass == 'G1TM', MdMaterial.subclass == 'G1TT'))
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_mass(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(and_(MdMaterial.subclass != 'IPAA',
                                              MdMaterial.subclass != 'MPMP', MdMaterial.subclass != None,
                                              MdMaterial.subclass != '', MdMaterial.subclass != 'G1TM',
                                              MdMaterial.subclass != 'G1TT', MdMaterial.material.not_like(
                                                  'CQ%'),
                                              MdMaterial.material.not_like(
                                                  'CW%'), MdMaterial.material.not_like('%0011'),
                                              MdMaterial.material.not_like('%0012')))
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_raw_material(db: AsyncSession) -> Optional[Material]:
        stmt = select(MdMaterial).filter(or_(MdMaterial.subclass == 'MPMP',
                                             MdMaterial.subclass == None, MdMaterial.subclass == ''))
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_tissues(db: AsyncSession, plant, year) -> Optional[Material]:
        query = f"""with mass as (
        select mes.tm_material, mes.plant,mes."year" from material_espec_std mes where mes."year" = {year} union 
        select mest.material, mest.plant,mest."year" from material_espec_std_tm mest where mest."year" = {year} union
        select mesm.material, mesm.plant,mesm."year" from material_espec_std_me mesm where mesm."year" = {year} union 
        select mez.material, mez.plant,mez."year" from material_espec_zp78 mez where mez."year" = {year} 
        ),
        totalcoststandard as(select distinct mes.tm_material, mes.plant, mes."year",
                       (case when mes.tm_material like 'C%' then (select
                                                            sum(mc.cost_std * mesm.raw_weight)/sum(mesm.raw_weight) as preco
                                                                from
                                                                    material_espec_std_me mesm
                                                                inner join material_cost mc
                                                                    on mesm.raw_material = mc.material
                                                                    and mesm."year" = mc."year" 
                                                                where
                                                                    mesm.raw_material not like 'RG%'
                                                                    and mesm.plant = mes.plant
                                                                    and mesm.material = mes.tm_material
                                                                    and mesm.year = {year}
                                                                    )
                            when mes.tm_material like 'S%' or mes.tm_material like 'Y%' then (
                                                               select cost_std * raw_weight as custo
                                                            from
                                                                material_espec_std_tm
                                                            inner join material_cost on
                                                                material_espec_std_tm.material = mes.tm_material
                                                                and material_espec_std_tm.raw_material = material_cost.material and
                                                                material_cost."year" = material_espec_std_tm."year" 
                                                            where
                                                                material_espec_std_tm.plant = mes.plant
                                                                and material_espec_std_tm.material = mes.tm_material and
                                                                material_espec_std_tm."year" = {year}
                                                                )
                         when mes.tm_material like 'RC%' then ( 
                                    select
                                        sum(mc.cost_std) as total
                                    from
                                        material_cost as mc
                                    where
                                        mc.material = mes.tm_material and
                                        mc."year" = {year}
                                        )
                        end) cost_std
                    from
                        mass mes                                       
                    where
                        mes.tm_material not like 'CQ%'
                        and mes.tm_material not like 'CW%'
                        and mes.tm_material not like '%0011'
                        and mes.tm_material not like '%0012'),                        
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
                                case when mez.month = '1' then (cost_m01 * mp_weight)
                                     when mez.month = '2' then (cost_m02 * mp_weight)
                                     when mez.month = '3' then (cost_m03 * mp_weight)
                                     when mez.month = '4' then (cost_m04 * mp_weight)
                                     when mez.month = '5' then (cost_m05 * mp_weight)
                                     when mez.month = '6' then (cost_m06 * mp_weight)
                                     when mez.month = '7' then (cost_m07 * mp_weight)
                                     when mez.month = '8' then (cost_m08 * mp_weight)
                                     when mez.month = '9' then (cost_m09 * mp_weight)
                                     when mez.month = '10' then (cost_m10 * mp_weight)
                                     when mez.month = '11' then (cost_m11 * mp_weight)
                                     when mez.month = '12' then (cost_m12 * mp_weight)
                                    end
                            from material_espec_zp78
                                inner join material_cost on material_espec_zp78.mat_mp = material_cost.material
                                where material_espec_zp78.material = mez.component limit 1
                        )
                        when mez.component like 'STT%' or mez.component like 'YTT%' then (
                             select
                                     case when mez.month = '1' then (cost_m01 * mp_weight)
                                     when mez.month = '2' then (cost_m02 * mp_weight)
                                     when mez.month = '3' then (cost_m03 * mp_weight)
                                     when mez.month = '4' then (cost_m04 * mp_weight)
                                     when mez.month = '5' then (cost_m05 * mp_weight)
                                     when mez.month = '6' then (cost_m06 * mp_weight)
                                     when mez.month = '7' then (cost_m07 * mp_weight)
                                     when mez.month = '8' then (cost_m08 * mp_weight)
                                     when mez.month = '9' then (cost_m09 * mp_weight)
                                     when mez.month = '10' then (cost_m10 * mp_weight)
                                     when mez.month = '11' then (cost_m11 * mp_weight)
                                     when mez.month = '12' then (cost_m12 * mp_weight)
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
                where
                    mez.component not like 'CQ%'
                    and mez.component not like 'CW%'
                    and mez.component not like '%0011'
                    and mez.component not like '%0012'
                    and mez.year = {year}
            ),
            tissue as(
                    select mm.material, mm.mat_desc,mest.plant,mest."year",'std' as month,  mest.comp_material as comp ,mest.raw_material as raw, mest.raw_weight, mest.comp_weight from md_material mm right join material_espec_std_tm mest
                    on mm.material = mest.material and mest."year" = {year} where mm.material like 'S%' or mm.material like 'Y%'
                    union
                    select mm.material, mm.mat_desc,mez.plant,mez."year", text(mez."month"), mez.mat_me as comp, mez.componente as raw, mez.mp_weight, mez.me_weight from md_material mm right join material_espec_zp58 mez
                    on mm.material = mez.material and mez."year" = {year} where mm.material like 'S%' or mm.material like 'Y%'
                    union
                    select mm.material, mm.mat_desc,mez78.plant,mez78."year", text(mez78."month"), mez78.mat_me as comp, mez78.mat_mp as raw, mez78.mp_weight, mez78.me_weight from md_material mm right join material_espec_zp78 mez78
                    on mm.material = mez78.material and mez78."year" = {year} where mm.material like 'S%' or mm.material like 'Y%')
            select material, year, mat_desc, plant,comp, raw,array_agg(jsonb_build_array("month",raw_weight,comp_weight,
            coalesce((select t.cost_std from totalcoststandard t where t.tm_material = tissue.material and t.plant = tissue.plant and tissue."month" = 'std' limit 1),0),
            coalesce((select t.cost_std from totalcoststandard t where t.tm_material = tissue.comp and t.plant = tissue.plant and tissue."month" = 'std' limit 1) * comp_weight,0),
            coalesce((select t2.cost_eff from totalcostseffective t2 where t2.component  = tissue.material and t2.plant = tissue.plant and text(t2."month") = tissue."month" limit 1),0),
            coalesce((select t2.cost_eff from totalcostseffective t2 where t2.component  = tissue.comp and t2.plant = tissue.plant and text(t2."month") = tissue."month" limit 1) * comp_weight,0))) from tissue group by material, year, mat_desc, plant,comp, raw
            """
        sqlQuery = text(query)
        resultQuery = await db.execute(sqlQuery)
        result = list(resultQuery)
        return result


    async def listRawMaterialRecipesByMonth(db: AsyncSession, plant, product, year) -> Optional[Material]:
        sqlQuery = """
            select
                distinct component,
                (
                    select
                        raw_weight
                    from
                        material_espec_std_me mesmstd
                    where
                        mesmstd.plant = '"""+plant+"""' and 
                        mesmstd.material = '"""+product+"""' and 
                        mesmstd.raw_material = tcomp.component and
                        mesmstd.year = """+year+""" limit 1
                ) as STD,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 01 and
                        mez2."year" = """+year+""" limit 1
                ) as M01,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 02 and
                        mez2."year" = """+year+""" limit 1
                ) as M02,
                    (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 03 and
                        mez2."year" = """+year+""" limit 1
                ) as M03,
                    (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 04 and
                        mez2."year" = """+year+""" limit 1
                ) as M04,
                    (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 05 and
                        mez2."year" = """+year+""" limit 1
                ) as M05,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 06 and
                        mez2."year" = """+year+""" limit 1
                ) as M06,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 06 and
                        mez2."year" = """+year+""" limit 1
                ) as M06,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 07 and
                        mez2."year" = """+year+""" limit 1
                ) as M07,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 08 and
                        mez2."year" = """+year+""" limit 1
                ) as M08,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 09 and
                        mez2."year" = """+year+""" limit 1
                ) as M09,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 10 and
                        mez2."year" = """+year+""" limit 1
                ) as M10,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 11 and
                        mez2."year" = """+year+""" limit 1
                ) as M11,
                (
                    select
                        qtd_without
                    from
                        material_espec_zp45 mez2 
                    where
                        mez2.plant = '"""+plant+"""' and 
                        mez2.material = '"""+product+"""' and 
                        mez2.component = tcomp.component and
                        mez2.subclass = 'MPMP' and 
                        mez2."month" = 12 and
                        mez2."year" = """+year+""" limit 1
                ) as M12
            from
                (
                select
                    raw_material as component
                from
                    material_espec_std_me mesm
                where
                    mesm.plant = '"""+plant+"""' and 
                    mesm.material = '"""+product+"""' and 
                    mesm."year" = """+year+"""
                union all
                select
                    component
                from
                    material_espec_zp45 mez left join md_material mm on mez.material = mm.material  left join market_segment ms on mm.mkg_segm = ms.mkg_segm
                where                
                mez.plant = '"""+plant+"""' and 
                mez.material = '"""+product+"""' and 
                mez."year" = """+year+""" and
            mez.subclass = 'MPMP') tcomp
        """
        resultQuery = await db.execute(sqlQuery)
        result = []

        for row in resultQuery:
            child = {'rawmaterial': row[0], 'months': []}
            for childrow in row:
                if(childrow is None):
                    child['months'].append({'material': 'undefined', 'cost_standard': '--', 'cost_effective': '--',
                                       'raw_weight': '--', 'total_cost_standard': '--', 'total_cost_effective': '--'})
                else:
                    child['months'].append({'material': row[0], 'cost_standard': 0, 'cost_effective': 0,
                                       'raw_weight': childrow, 'total_cost_standard': 0, 'total_cost_effective': 0})
            result.append(child)

        return result

    async def find_density(db: AsyncSession, plant, material, year, month) -> Optional[Material]:
        month = 'std'
        if(month == 'std'):
            sqlQuery = """ select coalesce (mez.dens_real ,mez.dens_theor) as DENSIDADE from material_espec_zp88 mez where mez.material = '""" + material + """' and mez.plant = '"""+ plant +"""' order by mez.dt_release desc limit 1 """
        else:
            sqlQuery = """SELECT
                                mesm.density
                            from
                                material_espec_std_me mesm
                            where
                                mesm.plant = '"""+ str(plant) +"""'
                                and mesm.material = '""" + str(material) + """'
                                and mesm."year" = '"""+ str(year) +"""' limit 1
                        """                
       

        result = await db.execute(sqlQuery)
        
        cost = [row[0] for row in result]
        if len(cost) <= 0 or cost[0] is None:
            return 0
        return cost[0]   
    
    
    async def rawWeightCalculate(db: AsyncSession, plant, material, rawMaterial, month, year, filterType, result) -> Optional[Material]:
        if(int(filterType) == 1 and re.search("^RG.+$",rawMaterial)):
            result = 0

        if(int(filterType) == 3):
            try:
                result = await repositories.material_especZp45.MaterialEspecZp45Repository.find_material_utilization(db,plant, material, rawMaterial, '02', year)
            except:
                result = Decimal(0)
        return result    

    async def find_by_materialtm(db: AsyncSession, plant, material, year) -> Optional[Material]:
        stmt = select(MaterialEspecStdTm).filter(MaterialEspecStdTm.plant == plant, 
                                                 MaterialEspecStdTm.material == material, 
                                                 MaterialEspecStdTm.year == year)
        result = await db.execute(stmt)
        return result.scalars().first()
    
    async def find_by_material58(db: AsyncSession, plant, material,month, year) -> Optional[MaterialEspecZp58]:
        stmt = select(MaterialEspecZp58).filter(MaterialEspecZp58.plant == plant, MaterialEspecZp58.material == material,MaterialEspecZp58.month == month,  MaterialEspecZp58.year == year)
        result = await db.execute(stmt)
        return result.scalars().first()


    async def find_by_material78(db: AsyncSession, plant, material, month, year) -> Optional[MaterialEspecZp78]:
        stmt = select(MaterialEspecZp78).filter(MaterialEspecZp78.plant == plant, MaterialEspecZp78.material == material, MaterialEspecZp78.month == month, MaterialEspecZp78.year == year)
        result = await db.execute(stmt)
        return result.scalars().first()
    
    
permission = MdMaterialRepository()
