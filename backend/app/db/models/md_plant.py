from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer


class MdPlant(Base):
    __tablename__ = "md_plant"

    id = Column(Integer, primary_key=True)
    plant = Column(String(length=40), nullable=False)
    plant_desc = Column(String(length=20), nullable=True)    
    

