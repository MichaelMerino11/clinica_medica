from app.database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Consulta(Base):
    __tablename__ = "consultas"
    
    id = Column(Integer, primary_key=True, index=True)
    cita_id = Column(Integer, ForeignKey("citas.id"))
    diagnostico = Column(Text)
    tratamiento = Column(Text)
    observaciones = Column(Text)
    
    cita = relationship("Cita", back_populates="consulta")
    prescripciones = relationship("Prescripcion", back_populates="consulta")
    ordenes_medicas = relationship("OrdenMedica", back_populates="consulta")
    certificado = relationship("Certificado", uselist=False, back_populates="consulta")

class Prescripcion(Base):
    __tablename__ = "prescripciones"
    
    id = Column(Integer, primary_key=True, index=True)
    consulta_id = Column(Integer, ForeignKey("consultas.id"))
    medicamento = Column(String(100))
    dosis = Column(String(50))
    frecuencia = Column(String(50))
    duracion = Column(String(50))
    
    consulta = relationship("Consulta", back_populates="prescripciones")

class OrdenMedica(Base):
    __tablename__ = "ordenes_medicas"
    
    id = Column(Integer, primary_key=True, index=True)
    consulta_id = Column(Integer, ForeignKey("consultas.id"))
    tipo = Column(String(50))  # laboratorio, imagenología, etc.
    descripcion = Column(Text)
    
    consulta = relationship("Consulta", back_populates="ordenes_medicas")