from sqlalchemy.orm import Session
from ..models.paciente import Paciente

class PacienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def crear_paciente(self, paciente: Paciente):
        self.db.add(paciente)
        self.db.commit()
        self.db.refresh(paciente)
        return paciente

    def obtener_paciente_por_cedula(self, cedula: str):
        return self.db.query(Paciente).filter(Paciente.cedula == cedula).first()