from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Text, Integer, DECIMAL, TIMESTAMP


class MaterialEspecZp88(Base):  
    __tablename__ = "material_espec_zp88"

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=True)
    month = Column(Integer, nullable=True)
    plant = Column(String(length=4), nullable=False, primary_key=True)
    material = Column(String(length=9), nullable=False, primary_key=True)
    document = Column(String(length=20), nullable=False, primary_key=True)
    utilization = Column(String(length=20), nullable=False, primary_key=True)
    charge = Column(DECIMAL(), nullable=False)
    quote = Column(Integer, nullable=False)
    charge_utilization = Column(DECIMAL(), nullable=False)
    recycle = Column(String(length=20), nullable=False)
    total_recycle = Column(DECIMAL(), nullable=False)
    status = Column(String(length=20), nullable=False)
    time = Column(DECIMAL(), nullable=False)
    machine = Column(String(length=20), nullable=False)
    dens_theor = Column(DECIMAL(), nullable=True)
    dens_real = Column(DECIMAL(), nullable=True)
    dt_phase = Column(TIMESTAMP(), nullable=True)
    dt_creation = Column(TIMESTAMP(), nullable=True)
    dt_release = Column(TIMESTAMP(), nullable=True)
    dt_expir = Column(TIMESTAMP(), nullable=True)
    rpm = Column(Integer, nullable=True)
    time_effect = Column(Integer, nullable=True)
    DT_PHASEOUT = Column(Integer, nullable=True)