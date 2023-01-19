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
    type: str,
    plant: str,
    market_segment: str,
    year: str,
    line: str,
    type_selected: str,
) -> Any:
    itens = await repositories.RawMaterialAndCompoundRepository.listComponents(db=db, type=type, plant=None, market_segment=None, line=None, year=year, type_selected=type_selected)
    total = await repositories.RawMaterialAndCompoundRepository.totalComponents(db=db, type=type, plant=None, market_segment=None, line=None, year=year, type_selected=type_selected)
    response = {
        'total': jsonable_encoder(total),
        'items': jsonable_encoder(itens),
    }
    return response