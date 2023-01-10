from typing import Optional
from pydantic import BaseModel



class MaterialEspecStdSc(BaseModel):
    td_material: str
    
    class Config:
        orm_mode = True
        
        