from typing import Optional
from pydantic import BaseModel



class MaterialEspecZp45Sc(BaseModel):
    plant: str
    material: str
    year: int
    month: int
    component: str
    document: str
    subclass: str
    cost_center: str
    workcenter: str
    team: float
    quote: int
    utilization: float
    measure_unit: str
    labor_main: float
    labor_auxiliary: float
    increase: float
    cycle: float
    expenditure: float
    family: str
    weight: float
    measure_weight: str
    qtd_without: float
    labor_main_base: float
    labor_auxiliary_base: float
    increase_base: float
    cycle_base: float
    expenditure_base: float
    
    class Config:
        orm_mode = True
        
    