from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Cita(Base):
    __tablename__ = "citas"
    
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    medico_id = Column(Integer, ForeignKey("medicos.id"))
    fecha_hora = Column(DateTime, default=datetime.now)
    estado = Column(String(20), default="PENDIENTE")  # PENDIENTE, CONFIRMADA, CANCELADA, ATENDIDA
    motivo = Column(String(200))
    
    paciente = relationship("Paciente", back_populates="citas")
    medico = relationship("Medico", back_populates="citas")
    consulta = relationship("Consulta", uselist=False, back_populates="cita")