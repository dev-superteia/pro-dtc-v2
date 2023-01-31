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
filter: str,
month: int,
year: int,
) -> Any:

    raw_materials_explosion = await repositories.rawMaterial.get_raw_material_list_explosion(db=db, plant=plant, materialName=product, filterType=filter, month=month, year=year)
    raw_materials_explision_calculate = await repositories.rawMaterial.get_calculate_totals_raw_material_list(db=db, listRawMaterial=raw_materials_explosion, plant=plant, material=product, year=year, month=month)  

    response = {
        'table': raw_materials_explision_calculate,
    }

    return jsonable_encoder(response)