from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    perfil = Column(String)  # "admin", "medico", "recepcionista"
    es_activo = Column(Boolean, default=True)

class ParametroGeneral(Base):
    __tablename__ = "parametros_generales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    valor = Column(String)