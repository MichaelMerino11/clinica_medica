from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Medico(Base):
    __tablename__ = "medicos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    especialidad = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

class Colaborador(Base):
    __tablename__ = "colaboradores"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    rol = Column(String)  # "recepcionista", "administrativo"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))