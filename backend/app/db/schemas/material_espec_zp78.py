from typing import Optional
from pydantic import BaseModel



class MaterialEspecZp78Sc(BaseModel):
    plant: str
    material: str
    year: int
    month: int
    tm_weight: float
    mp_weight: float
    me_weight: float
    mat_mp: str
    mat_me: str
    mat_me_weight: float
    total_weight: float
    
    class Config:
        orm_mode = True
        
