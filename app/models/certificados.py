from app.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime


class Certificado(Base):
    __tablename__ = "certificados"
    
    id = Column(Integer, primary_key=True, index=True)
    consulta_id = Column(Integer, ForeignKey("consultas.id"))
    contenido = Column(Text)
    fecha_emision = Column(DateTime, default=datetime.now)
    codigo_verificacion = Column(String(50), unique=True)
    
    consulta = relationship("Consulta", back_populates="certificado")