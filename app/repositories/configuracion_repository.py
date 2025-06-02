from sqlalchemy.orm import Session
from ..models.configuracion import Usuario

class ConfiguracionRepository:
    def __init__(self, db: Session):
        self.db = db

    def obtener_usuario_por_email(self, email: str):
        return self.db.query(Usuario).filter(Usuario.email == email).first()

    def crear_usuario(self, usuario: Usuario):
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario