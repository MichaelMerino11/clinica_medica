from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Reporte, Consulta, Paciente
from ..auth import verificar_token

router = APIRouter(prefix="/reportes", tags=["Reportes"])

@router.get("/libro-diario")
def libro_diario(fecha: str, db: Session = Depends(get_db)):
    # Implementación alternativa si necesitas transacciones
    return {"message": "Endpoint de reporte libro diario"}

@router.get("/historia-clinica/{paciente_id}")
def historia_clinica(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    consultas = db.query(Consulta).filter(Consulta.paciente_id == paciente_id).all()
    
    return {
        "paciente": paciente,
        "consultas": consultas
    }