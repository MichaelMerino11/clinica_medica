from ..repositories.configuracion_repository import ConfiguracionRepository
from ..models.configuracion import Usuario

class ConfiguracionService:
    def __init__(self, db):
        self.repository = ConfiguracionRepository(db)

    def crear_usuario(self, email: str, password: str, perfil: str):
        usuario = Usuario(email=email, password=password, perfil=perfil)
        return self.repository.crear_usuario(usuario)