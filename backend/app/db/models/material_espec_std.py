from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL


class MaterialEspecStd(Base):  
    __tablename__ = "material_espec_std"

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False, primary_key=True)
    plant = Column(String(length=4), nullable=False, primary_key=True)
    material = Column(String(length=9), nullable=False, primary_key=True)
    tm_material = Column(String(length=9), nullable=False, primary_key=True)
    weight = Column(DECIMAL(), nullable=False)