from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL


class MarketCost(Base):  
    __tablename__ = "material_cost"

    year = Column(Integer, nullable=False, primary_key=True)
    id = Column(Integer, primary_key=True)
    material = Column(String(length=9), nullable=False, primary_key=True)
    description = Column(String(length=200), nullable=True)
    cost_std = Column(DECIMAL(), nullable=False)
    cost_m01 = Column(DECIMAL(), nullable=False)
    cost_m02 = Column(DECIMAL(), nullable=False)
    cost_m03 = Column(DECIMAL(), nullable=False)
    cost_m04 = Column(DECIMAL(), nullable=False)
    cost_m05 = Column(DECIMAL(), nullable=False)
    cost_m06 = Column(DECIMAL(), nullable=False)
    cost_m07 = Column(DECIMAL(), nullable=False)
    cost_m08 = Column(DECIMAL(), nullable=False)
    cost_m09 = Column(DECIMAL(), nullable=False)
    cost_m10 = Column(DECIMAL(), nullable=False)
    cost_m11 = Column(DECIMAL(), nullable=False)
    cost_m12 = Column(DECIMAL(), nullable=False)
    cost_b01 = Column(DECIMAL(), nullable=True)
    cost_b02 = Column(DECIMAL(), nullable=True)
    cost_b03 = Column(DECIMAL(), nullable=True)
    cost_b04 = Column(DECIMAL(), nullable=True)
    cost_b05 = Column(DECIMAL(), nullable=True)
    cost_b06 = Column(DECIMAL(), nullable=True)
    cost_b07 = Column(DECIMAL(), nullable=True)
    cost_b08 = Column(DECIMAL(), nullable=True)
    cost_b09 = Column(DECIMAL(), nullable=True)
    cost_b10 = Column(DECIMAL(), nullable=True)
    cost_b11 = Column(DECIMAL(), nullable=True)
    cost_b12 = Column(DECIMAL(), nullable=True)