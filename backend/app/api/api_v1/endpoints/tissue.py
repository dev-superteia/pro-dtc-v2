from typing import Any, List
from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas, models
from app.api import deps
from fastapi_redis_cache import cache_one_day, cache_one_day
from fastapi.encoders import jsonable_encoder

router = APIRouter()


# TODO:Colocar em um novo arquivo
@router.get("/", response_model=List[schemas.Tissue])
async def get_raw(
    response: Response,
    plant: str,
    year: str,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    print(plant == 'undefined')
    #raw = await repositories.MdMaterialRepository.get_raw(db=db)
    raw = {}
    return jsonable_encoder(raw)