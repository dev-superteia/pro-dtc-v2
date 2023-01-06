from typing import Any, Optional
from sqlalchemy import select
from app.db.models.market_segment import MarketSegment
from app.db.schemas import MarketSegmentSc, MarketSegmentAll
from sqlalchemy.ext.asyncio import AsyncSession


class MarketSegmentRepository():
    async def get(db: AsyncSession) -> Optional[MarketSegmentAll]:
        stmt = select(MarketSegment).offset(0).limit(100)
        result = await db.execute(stmt)
        return result.scalars().all()
    
    async def get_line(db: AsyncSession) -> Optional[MarketSegmentSc]:
        stmt = select(MarketSegment).distinct(MarketSegment.line).order_by(MarketSegment.line)
        result = await db.execute(stmt)
        return result.scalars().all()


permission = MarketSegmentRepository()
