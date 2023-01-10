from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL


class MaterialEspecZp45(Base):  
    __tablename__ = "material_espec_zp45"

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=True)
    month = Column(Integer, nullable=True)
    plant = Column(String(length=4), nullable=False, primary_key=True)
    material = Column(String(length=9), nullable=False, primary_key=True)
    component = Column(String(length=9), nullable=False, primary_key=True)
    document = Column(String(length=20), nullable=True)
    subclass = Column(String(length=4), nullable=True)
    cost_center = Column(String(length=4), nullable=True)
    workcenter = Column(String(length=4), nullable=True)
    team = Column(DECIMAL(), nullable=True)
    quote = Column(Integer, nullable=True)
    utilization = Column(DECIMAL(), nullable=True)
    measure_unit = Column(String(length=3), nullable=True)
    labor_main = Column(DECIMAL(), nullable=True)
    labor_auxiliary = Column(DECIMAL(), nullable=True)
    increase = Column(DECIMAL(), nullable=True)
    cycle = Column(DECIMAL(), nullable=True)
    expenditure = Column(DECIMAL(), nullable=True)
    family = Column(String(length=2), nullable=True)
    weight = Column(DECIMAL(), nullable=True)
    measure_weight = Column(String(length=3), nullable=True)
    qtd_without = Column(DECIMAL(), nullable=True)
    labor_main_base = Column(DECIMAL(), nullable=True)
    labor_auxiliary_base = Column(DECIMAL(), nullable=True)
    increase_base = Column(DECIMAL(), nullable=True)
    cycle_base = Column(DECIMAL(), nullable=True)
    expenditure_base = Column(DECIMAL(), nullable=True)