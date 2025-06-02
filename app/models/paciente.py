from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Paciente(Base):
    __tablename__ = "pacientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    cedula = Column(String(20), unique=True)
    telefono = Column(String(20))
    email = Column(String(100))
    fecha_nacimiento = Column(String(10))  # formato YYYY-MM-DD
    
    citas = relationship("Cita", back_populates="paciente")
    facturacion_terceros = relationship("FacturacionTerceros", back_populates="paciente")
    comprobantes = relationship("Comprobante", back_populates="paciente")

class FacturacionTerceros(Base):
    __tablename__ = "facturacion_terceros"
    
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    nombre = Column(String(100))
    ruc = Column(String(20))
    direccion = Column(String(200))
    
    paciente = relationship("Paciente", back_populates="facturacion_terceros")