from typing import Any, Optional
from pydantic import BaseModel



class RawMaterialAndCompound(BaseModel):
    plant: str
    year: str
    type: str
    typeSelected: str
    line: str
    
    class Config:
        orm_mode = True
