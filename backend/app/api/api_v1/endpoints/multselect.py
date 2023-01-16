from typing import Any, List
from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas
from app.api import deps
from fastapi_redis_cache import cache_one_day, cache_one_day
from fastapi.encoders import jsonable_encoder


router = APIRouter()

@router.get("/plant", response_model=List[schemas.Plant])
async def get_plant(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    plant = await repositories.MDplantRepository.get(db=db)
    print(plant)
    return plant

@router.get("/market_segment", response_model=List[schemas.MarketSegmentAll])
async def get_mkg(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    mkg = await repositories.MarketSegmentRepository.get(db=db)
    return mkg

@router.get("/line", response_model=List[schemas.MarketSegmentSc])
async def get_line(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    line = await repositories.MarketSegmentRepository.get_line(db=db)
    return line

@router.get("/tires", response_model=List[schemas.Material])
async def get_tires(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    tires = await repositories.MdMaterialRepository.get_tires(db=db)
    return tires


@router.get("/tissue", response_model=List[schemas.Material])
async def get_tissue(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    tissue = await repositories.MdMaterialRepository.get_tissue(db=db)
    return tissue

@router.get("/all_mass", response_model=List[schemas.Material])
async def all_mass(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    tissue = await repositories.MdMaterialRepository.all_mass(db=db)
    return tissue

@router.get("/mass", response_model=List[schemas.Material])
async def get_mass(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    tissue = await repositories.MdMaterialRepository.get_mass(db=db)
    return tissue

@router.get("/raw_material", response_model=List[schemas.Material])
async def get_raw_material(
    response: Response,
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Retrieve all available user roles.
    """
    raw = await repositories.MdMaterialRepository.get_raw_material(db=db)
    return jsonable_encoder(raw)
    
   