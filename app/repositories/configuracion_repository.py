from sqlalchemy.orm import Session
from ..models.configuracion import Usuario, ParametroGeneral

class ConfiguracionRepository:
    def __init__(self, db: Session):
        self.db = db

    def crear_usuario(self, usuario: Usuario):
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario