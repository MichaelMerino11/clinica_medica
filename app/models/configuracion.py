from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    perfil = Column(String)  # "admin", "medico", "recepcionista"
    es_activo = Column(Boolean, default=True)

    def verificar_password(self, password: str):
        return pwd_context.verify(password, self.password)
    
    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)

class ParametroGeneral(Base):
    __tablename__ = "parametros_generales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    valor = Column(String)