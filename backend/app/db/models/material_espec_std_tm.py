from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL


class MaterialEspecStdTm(Base):  
    __tablename__ = "material_espec_std_tm"

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False, primary_key=True)
    plant = Column(String(length=4), nullable=False, primary_key=True)
    material = Column(String(length=9), nullable=False, primary_key=True)
    espec = Column(String(length=20), nullable=False, primary_key=True)
    raw_material = Column(
        String(length=9), nullable=False, primary_key=True)
    comp_material = Column(
        String(length=9), nullable=False, primary_key=True)
    raw_weight = Column(DECIMAL(), nullable=False)
    comp_weight = Column(DECIMAL(), nullable=False)