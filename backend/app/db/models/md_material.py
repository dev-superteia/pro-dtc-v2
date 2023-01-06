from app.db.base_class import Base
from sqlalchemy import Column, String, Integer

class MdMaterial(Base):
    __tablename__ = "md_material"

    id = Column(Integer, primary_key=True)
    material = Column(String(length=9), nullable=False, primary_key=True)
    mat_desc = Column(String(length=40), nullable=False, primary_key=True)
    subclass = Column(String(length=50), nullable=False)
    family = Column(String(length=50), nullable=False)
    mkg_segm = Column(String(length=4), nullable=True)
