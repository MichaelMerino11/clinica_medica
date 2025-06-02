from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Medico(Base):
    __tablename__ = "medicos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(50))
    matricula = Column(String(20), unique=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    citas = relationship("Cita", back_populates="medico")

class Colaborador(Base):
    __tablename__ = "colaboradores"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    rol = Column(String(50))  # enfermero/a, recepcionista, etc.
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))