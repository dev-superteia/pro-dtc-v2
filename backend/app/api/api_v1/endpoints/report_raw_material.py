from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas, models
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.PlantInDBBase])
async def get(
    *,
    db: AsyncSession = Depends(deps.get_db),
    plant: str,
    year: int,
) -> Any:
    result = await repositories.MaterialCostRepository.is_cost_null(db=db, plant=plant, year=year)
    return result