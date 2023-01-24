from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas, models
from app.api import deps
from fastapi.encoders import jsonable_encoder
router = APIRouter()

@router.get("/")
async def get(
    *,
    db: AsyncSession = Depends(deps.get_db),
    plant: str,
    product: str,
    year: str,
    market_segment: str,
    line: str,
) -> Any:

    typex = 1

    periods = [
        {'month': 'std', 'components': {}},
        {'month': '01', 'components': {}},
        {'month': '02', 'components': {}},
        {'month': '03', 'components': {}},
        {'month': '04', 'components': {}},
        {'month': '05', 'components': {}},
        {'month': '06', 'components': {}},
        {'month': '07', 'components': {}},
        {'month': '08', 'components': {}},
        {'month': '09', 'components': {}},
        {'month': '10', 'components': {}},
        {'month': '11', 'components': {}},
        {'month': '12', 'components': {}}
    ]

    raw_materials = []
    return_table = []

    for period in periods:
        if period['month'] != 'std':
            table = await repositories.ProductRawMaterialRepository.productExplodeZp45(db=db, plant=plant, product=product, month=period['month'], year=year, type=typex, market_segment=None, line=None)
        else:
            table = await repositories.MaterialEspecStdRepository.productExplode(db=db, plant=plant, product=product, month=period['month'], year=year, type=typex, market_segment=None, line=None)

    if len(table) > 0:
        for auxmaterial in table:
            raw_materials.append(auxmaterial['material'])
            composition = {}
            # Calculate values by material - Modal
            for x in auxmaterial['tm_composition']:
                values = x.split(';')
                print(values)
                values = [values[0]] + [float(x) if x != '' else 0 for x in values[1:]]
                if composition.get(values[0]) and period['month'] != 'std':
                    composition[values[0]]['raw_weight_volum'] += values[4]
                    composition[values[0]]['totalcoststandard_volum'] += values[5]
                    composition[values[0]]['totalcosteffective_volum'] += values[6]
                else:
                    composition[values[0]] = {}
                    composition[values[0]]['raw_weight'] = values[1]
                    composition[values[0]]['totalcoststandard'] = values[2]
                    composition[values[0]]['totalcosteffective'] = values[3]
                    if period['month'] != 'std':
                        composition[values[0]]['raw_weight_volum'] = values[4]
                        composition[values[0]]['totalcoststandard_volum'] = values[5]
                        composition[values[0]]['totalcosteffective_volum'] = values[6]
            auxmaterial = dict(auxmaterial)
            auxmaterial['tm_composition'] = composition

            # Add component values of the actual month
            period['components'][auxmaterial['material']] = auxmaterial

    # Get distinct raw materials
    RawMaterials = list(filter(None, dict.fromkeys([row for row in raw_materials])))

    for mataux in RawMaterials:
        months = []

        # Alocate values by month of each raw material
        for period in periods:
            months.append(period['components'].get(mataux, {}))

        return_table.append({'material': mataux, 'values': months})

    return (return_table)