from typing import Optional
from pydantic import BaseModel



class Plant(BaseModel):
    plant: str
    plant_desc: str
    
    class Config:
        orm_mode = True

