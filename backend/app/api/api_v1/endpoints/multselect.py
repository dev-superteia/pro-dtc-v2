from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas, models
from app.api import deps

router = APIRouter()

@router.get("/plant", response_model=List[schemas.Plant])
async def get_plant(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    permissions = await repositories.MDplantRepository.get(db=db)
    return permissions

@router.get("/market_segment", response_model=List[schemas.MarketSegmentAll])
async def get_mkg(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    permissions = await repositories.MarketSegmentRepository.get(db=db)
    return permissions

@router.get("/line", response_model=List[schemas.MarketSegmentSc])
async def get_line(
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Retrieve all available user roles.
    """
    permissions = await repositories.MarketSegmentRepository.get_line(db=db)
    return permissions