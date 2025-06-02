from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    cedula = Column(String, unique=True)
    telefono = Column(String)
    email = Column(String, nullable=True)

    facturacion_terceros = relationship("FacturacionTerceros", back_populates="paciente")

class FacturacionTerceros(Base):
    __tablename__ = "facturacion_terceros"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    nombre = Column(String)
    ruc = Column(String)
    direccion = Column(String)
    
    paciente = relationship("Paciente", back_populates="facturacion_terceros")