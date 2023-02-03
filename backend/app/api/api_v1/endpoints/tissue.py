from typing import Any, List
from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas, models
from app.api import deps
from fastapi_redis_cache import cache_one_day,cache_one_minute
from fastapi.encoders import jsonable_encoder

router = APIRouter()


# TODO:Colocar em um novo arquivo
@router.get("/", response_model=List[schemas.Tissue])
@cache_one_minute()
async def get_raw(
    response: Response,
    plant: str,
    year: str,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    raw = await repositories.MdMaterialRepository.get_tissues(db=db, plant=plant,year=year)
    #raw = {}
    return jsonable_encoder(raw)

@router.get("/report_raw_material_month_tissue", response_model=List[schemas.Tissue])
async def get_tissue(
    *,
    db: AsyncSession = Depends(deps.get_db),
    plant: str,
    material: str,
    year: int,
    ) -> Any:
    
    result = []
    # Get each month values
    for month in range(0, 13):

        classCloth = repositories.Tissue(plant, material, 1, month, year)        

        result_month = await repositories.tissue.get_cloth_month(classCloth,db)
        if result_month['status']:
            result.append({'status': True, 'month': month, 'card': repositories.tissue.table_presentation_convert_in_card(db, classCloth)})
        else:
            result.append({'status': False, 'month': month, 'card': []})

    return jsonable_encoder(result)