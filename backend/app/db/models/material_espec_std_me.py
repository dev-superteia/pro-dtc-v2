from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL


class MaterialEspecStdMe(Base):  
    __tablename__ = "material_espec_std_me"

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False, primary_key=True)
    plant = Column(String(length=4), nullable=False, primary_key=True)
    material = Column(String(length=9), nullable=False, primary_key=True)
    espec = Column(String(length=20), nullable=False, primary_key=True)
    raw_material = Column(String(length=9), nullable=True)
    raw_weight = Column(DECIMAL(), nullable=False)
    density = Column(DECIMAL(), nullable=False)