from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey  # Añadir ForeignKey
from app.database import Base
from datetime import datetime

class Reporte(Base):
    __tablename__ = "reportes"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50))  # LIBRO_DIARIO, HISTORIA_CLINICA, etc.
    fecha_generacion = Column(DateTime, default=datetime.now)
    parametros = Column(Text)  # JSON con parámetros del reporte
    contenido = Column(Text)   # Puede ser HTML, PDF en base64, etc.
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))