from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import repositories, schemas, models
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.RawMaterialAndCompound])
async def get(
    *,
    db: AsyncSession = Depends(deps.get_db),
    type: str,
    plant: str,
    market_segment: str,
    year: str,
    line: str,
    type_selected: str,
) -> Any:
    result = await repositories.RawMaterialAndCompoundRepository.listComponents(db=db, type=type, plant=plant, market_segment=market_segment, line=line, year=year, type_selected=type_selected)
    return result