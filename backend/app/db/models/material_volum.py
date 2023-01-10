from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL, TIMESTAMP


class MaterialVolum(Base):  
    __tablename__ = "material_volum"

    id = Column(Integer, primary_key=True)
    plant = Column(String(length=4), nullable=False, primary_key=True)
    year = Column(Integer, nullable=False, primary_key=True)
    month = Column(Integer, nullable=False, primary_key=True)
    dt_datetime = Column(TIMESTAMP(), nullable=False)
    warehouse = Column(String(length=4), nullable=False)
    material = Column(String(length=9), nullable=False, primary_key=True)
    total_volum = Column(Integer, nullable=False)
    total_value = Column(DECIMAL(), nullable=False)