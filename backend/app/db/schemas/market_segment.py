from typing import Optional
from pydantic import BaseModel



class MarketSegmentSc(BaseModel):
    line: str
    
    class Config:
        orm_mode = True
        
        
class MarketSegmentAll(MarketSegmentSc):
    mkg_segm: str
    bu: str
    denomination: str