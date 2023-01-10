from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL


class MaterialEspecZp58(Base):  
    __tablename__ = "material_espec_zp58"

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=True)
    month = Column(Integer, nullable=True)
    plant = Column(String(length=4), nullable=False, primary_key=True)
    material = Column(String(length=9), nullable=False, primary_key=True)
    tt_weight = Column(DECIMAL(), nullable=False)
    mp_weight = Column(DECIMAL(), nullable=False)
    me_weight = Column(DECIMAL(), nullable=False)
    componente = Column(String(length=9), nullable=False, primary_key=True)
    thickness = Column(Integer, nullable=False)
    mat_me = Column(String(length=9), nullable=False)
    fol_inf_thick = Column(DECIMAL(), nullable=True)
    fol_sup_thick = Column(DECIMAL(), nullable=True)
    text_weight = Column(DECIMAL(), nullable=False)
    mat_me_weight = Column(DECIMAL(), nullable=False)
    text_thick = Column(Integer, nullable=False)
    total_weight = Column(DECIMAL(), nullable=False)
    distinct_wire = Column(String(length=30), nullable=True)
    status = Column(String(length=4), nullable=False)
    emb_speed = Column(Integer, nullable=False)