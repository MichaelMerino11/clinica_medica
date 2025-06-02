from ..models.configuracion import Usuario
from ..repositories.configuracion_repository import ConfiguracionRepository

class ConfiguracionService:
    def __init__(self, db):
        self.repository = ConfiguracionRepository(db)

    def autenticar_usuario(self, email: str, password: str):
        usuario = self.repository.obtener_usuario_por_email(email)
        if not usuario or not usuario.verificar_password(password):
            return None
        return usuario

    def crear_usuario(self, email: str, password: str, perfil: str):
        usuario = Usuario(
            email=email,
            password=Usuario.hash_password(password),
            perfil=perfil
        )
        return self.repository.crear_usuario(usuario)