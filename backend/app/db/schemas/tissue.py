from typing import Optional,List
from pydantic import BaseModel



class Tissue(BaseModel):
    comp: str
    mat_desc: str
    material: str
    plant: str
    raw: str
    year: str
    array_agg: list
    class Config:
        orm_mode = True

