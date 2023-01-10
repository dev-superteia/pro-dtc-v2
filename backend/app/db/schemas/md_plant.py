from typing import Any, Optional
from pydantic import BaseModel



class Plant(BaseModel):
    plant: str
    plant_desc: str
    
    class Config:
        orm_mode = True

class PlantInDBBase(BaseModel):
    material: Any
    plant: Any
    year: Any
