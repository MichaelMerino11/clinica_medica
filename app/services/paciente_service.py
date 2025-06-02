from ..models.paciente import Paciente
from ..repositories.paciente_repository import PacienteRepository

class PacienteService:
    def __init__(self, db):
        self.repository = PacienteRepository(db)

    def crear_paciente(self, nombre: str, cedula: str, telefono: str):
        paciente = Paciente(
            nombre=nombre,
            cedula=cedula,
            telefono=telefono
        )
        return self.repository.crear_paciente(paciente)

    def obtener_paciente(self, cedula: str):
        return self.repository.obtener_paciente_por_cedula(cedula)