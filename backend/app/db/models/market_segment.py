from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer


class MarketSegment(Base):  
    __tablename__ = "market_segment"
    
    id = Column(Integer, primary_key=True)
    mkg_segm = Column(String(length=4), primary_key=True)
    line = Column(String(length=40), nullable=False)
    bu = Column(String(length=10), nullable=True)
    denomination = Column(String(length=40), nullable=True)