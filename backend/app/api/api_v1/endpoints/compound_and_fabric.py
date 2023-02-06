from typing import Any, List
from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas, models
from app.api import deps
from fastapi_redis_cache import cache_one_day,cache_one_minute
from fastapi.encoders import jsonable_encoder
from decimal import Decimal
router = APIRouter()


# TODO:Colocar em um novo arquivo
@router.get("/")
#@cache_one_minute()
async def get_raw(
    response: Response,
    plant: str,
    year: str,
    material: str,
    type: str,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    month = '02'

    table = await repositories.MdMaterialRepository.listRawMaterialRecipesByMonth(db=db,plant=plant, product=material, year=year)

    density = await repositories.MdMaterialRepository.find_density(db, plant, material, year, month)

    total_weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cost_list = ["cost_m01","cost_m02","cost_m03","cost_m04","cost_m05","cost_m06","cost_m07","cost_m08","cost_m09","cost_m10","cost_m11","cost_m12"]
    
    for years in table:
        text = await repositories.MaterialCostRepository.description(db,years['rawmaterial'])
        years['rawmaterial'] = years['rawmaterial']  + ' - ' +  str(text[0][0])
        for idx, months in enumerate(years['months']):
            if months['material'] != 'undefined':
                months['raw_weight'] = await repositories.MdMaterialRepository.rawWeightCalculate(db,plant, material, months['material'], month, year, type, months['raw_weight'])
                if idx == 1:
                    months['cost_standard'] = await repositories.MaterialCostRepository.find_by_material(db,material=months['material'], cost='cost_std')
                    months['cost_effective'] = await repositories.MaterialCostRepository.find_by_material(db,material=months['material'], cost='cost_std')
                    months['total_cost_standard'] = Decimal(months['cost_standard']) * Decimal(months['raw_weight']) 
                    months['total_cost_effective'] = Decimal(months['cost_effective']) * Decimal(months['raw_weight']) 
                    months['measure_unit'] = 'KG'
                    total_weights[0] += months['raw_weight']
                elif idx >= 2:
                    months['cost_standard'] = await repositories.MaterialCostRepository.find_by_material(db,material=months['material'], cost='cost_std')
                    print("oiiii",idx)
                    months['cost_effective'] = await repositories.MaterialCostRepository.find_by_material(db,material=months['material'], cost=cost_list[idx-3])
                    months['total_cost_standard'] = Decimal(months['cost_standard']) * Decimal(months['raw_weight']) 
                    months['total_cost_effective'] = Decimal(months['cost_effective']) * Decimal(months['raw_weight']) 
                    months['measure_unit'] = 'KG'
                    total_weights[idx-2] += months['raw_weight']
                    
    response = {
        'name': 'ok',
        'density': density,
        'weights': total_weights,
        'table': table,
        'total': []
    }

    return response
