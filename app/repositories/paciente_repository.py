from sqlalchemy.orm import Session
from ..models.paciente import Paciente, FacturacionTerceros

class PacienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def crear_paciente(self, paciente: Paciente):
        self.db.add(paciente)
        self.db.commit()
        self.db.refresh(paciente)
        return paciente