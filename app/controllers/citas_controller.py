from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.citas import Cita
from ..auth import verificar_token
from datetime import datetime

router = APIRouter(prefix="/citas", tags=["Citas"])

@router.get("/paciente/{cedula}")
def obtener_citas(cedula: str, db: Session = Depends(get_db)):
    citas = db.query(Cita).join(Paciente).filter(Paciente.cedula == cedula).all()
    return {
        "pendientes": [c for c in citas if c.estado == "PENDIENTE"],
        "atendidas": [c for c in citas if c.estado == "ATENDIDA"],
        "canceladas": [c for c in citas if c.estado == "CANCELADA"]
    }

@router.post("/")
def crear_cita(paciente_id: int, medico_id: int, fecha_hora: datetime,
               db: Session = Depends(get_db), token: str = Depends(verificar_token)):
    cita = Cita(paciente_id=paciente_id, medico_id=medico_id, 
                fecha_hora=fecha_hora, estado="PENDIENTE")
    db.add(cita)
    db.commit()
    return {"message": "Cita creada"}