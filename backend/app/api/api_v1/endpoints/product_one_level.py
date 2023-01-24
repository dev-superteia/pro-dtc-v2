from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas, models
from app.api import deps
from fastapi.encoders import jsonable_encoder
import re

router = APIRouter()

@router.get("/")
async def get(
    *,
    db: AsyncSession = Depends(deps.get_db),
    plant: str,
    product: str,
    market_segment: str,
    year: str,
    line: str,
) -> Any:

    table = await repositories.MaterialEspecStdRepository.listMaterialRecipesByMonth(db=db, plant=plant, product=product, year=year, market_segment=None, line=None)

    # Get distinct materials
    materials = list(set([x['material'] for x in table]))

    result = {}

    for material in materials:
        isTissue = 0
        mat_me = ""
        # Add informations if materials is a tissue
        if re.search("^(S|Y).+$", material):
            isTissue = 1
            mat_me = await repositories.MaterialEspecStdRepository.find_name_tissue(db=db, plant=None, material=None, tm_material=material, type='std', year=None)
            if mat_me == ' ':
                mat_me = await repositories.MaterialEspecStdRepository.find_name_tissue(db=db, plant=None, material=None, tm_material=material, type=None, year=None)

        result[material] = {'type': isTissue, 'mat_me': mat_me,
                            'months': [{} for _ in range(0, 13)]}

    m1 = list()
    m2 = list()
    # Add values of each month
    for row in table:
        month = 0 if row['month'] == 'std' else int(row['month'])
        result[row['material']]['months'][month] = row
    for material in materials:
        for x in range(1, 13):
            if(result[material]['months'][x]  == {}):
                if result[material]['months'][0]:
                    result[material]['months'][x]['month'] = x
                    result[material]['months'][x]['dtc'] = result[material]['months'][0].material_cost_1_tire_standard - 0
            if(result[material]['months'][x]  != {}):                  
                if result[material]['months'][x]['dtc'] == None:     
                    if result[material]['months'][0]:
                        if result[material]['months'][0]['material_cost_1_tire_standard'] == None:
                            result[material]['months'][x] = {
                            "amount_in_tire_kg": 0,                               
                            "amount_used_eff": 0,                               
                            "amount_used_eff_volum": 0,                               
                            "amount_used_std":0,                               
                            "amount_used_std_volum": 0,                             
                            "dtc_volum": 0,
                            "dtc": 0,
                            "material": material,
                            "material_cost_1_tire_effective": 0,
                            "material_cost_1_tire_effective_volum":0,
                            "material_cost_1_tire_standard": 0,
                            "material_cost_1_tire_standard_volum": 0,
                            "month": result[material]['months'][x]['month'],
                            "totalcosteff": 0,
                            "totalcosteff_volum": 0,
                            "totalcoststd": 0,
                            "totalcoststd_volum": 0                                 
                        }                                                    
                        else:
                            result[material]['months'][x]['dtc']                               
                    else:
                        dtc = 0
                        if result[material]['months'][x]['material_cost_1_tire_standard']:
                            dtc = result[material]['months'][x]['material_cost_1_tire_standard']
                        result[material]['months'][x] = {
                            "amount_in_tire_kg": result[material]['months'][x]['amount_in_tire_kg'],                               
                            "amount_used_eff": result[material]['months'][x]['amount_used_eff'],                               
                            "amount_used_eff_volum": result[material]['months'][x]['amount_used_eff_volum'],                               
                            "amount_used_std": result[material]['months'][x]['amount_used_std'],                               
                            "amount_used_std_volum": result[material]['months'][x]['amount_used_std_volum'],                             
                            "dtc_volum": 0,
                            "dtc":  dtc,
                            "material": material,
                            "material_cost_1_tire_effective": result[material]['months'][x]['material_cost_1_tire_effective'],
                            "material_cost_1_tire_effective_volum": result[material]['months'][x]['material_cost_1_tire_effective_volum'],
                            "material_cost_1_tire_standard": result[material]['months'][x]['material_cost_1_tire_standard'],
                            "material_cost_1_tire_standard_volum": result[material]['months'][x]['material_cost_1_tire_standard_volum'],
                            "month": result[material]['months'][x]['month'],
                            "totalcosteff": result[material]['months'][x]['totalcosteff'],
                            "totalcosteff_volum": result[material]['months'][x]['totalcosteff_volum'],
                            "totalcoststd": result[material]['months'][x]['totalcoststd'],
                            "totalcoststd_volum": result[material]['months'][x]['totalcoststd_volum']                               
                        }                    
    volums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Calculate volum of materials

    resul = await repositories.MaterialVolumRepository.list_volum_by_month(db=db, plant=plant, product=product, year=year, market_segment=market_segment, line=line)
    
    for row in resul:
            volums[row['month']] = row['volum']
            values[row['month']] = row['value']

    materialVolumTotals = {'volum': volums, 'value': values}
    response = {
            'volumTotais': materialVolumTotals,
            # 'itemsC': list(result),
            'items': result,
    }
    return jsonable_encoder(response)