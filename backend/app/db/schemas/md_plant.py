from typing import Any, Optional
from pydantic import BaseModel



class Plant(BaseModel):
    plant: str
    plant_desc: str
    
    class Config:
        orm_mode = True

class PlantInDBBase(BaseModel):
    component: Any
    plant: Any
    year: Any
