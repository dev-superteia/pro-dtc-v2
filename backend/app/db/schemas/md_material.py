from typing import Optional
from pydantic import BaseModel



class Material(BaseModel):
    material: str
    mat_desc: str
    
    class Config:
        orm_mode = True

