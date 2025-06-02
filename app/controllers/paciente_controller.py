from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.paciente_service import PacienteService
from ..database import get_db

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

@router.post("/")
def crear_paciente(nombre: str, cedula: str, telefono: str, db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.crear_paciente(nombre, cedula, telefono)