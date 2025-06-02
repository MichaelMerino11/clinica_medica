from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.consultas import Consulta, Prescripcion, OrdenMedica
from ..auth import verificar_token

router = APIRouter(prefix="/consultas", tags=["Consultas"])

@router.post("/")
def registrar_consulta(cita_id: int, diagnostico: str,
                      db: Session = Depends(get_db), token: str = Depends(verificar_token)):
    consulta = Consulta(cita_id=cita_id, diagnostico=diagnostico)
    db.add(consulta)
    db.commit()
    return {"message": "Consulta registrada"}

@router.post("/prescripciones")
def crear_prescripcion(consulta_id: int, medicamento: str, dosis: str,
                      db: Session = Depends(get_db), token: str = Depends(verificar_token)):
    prescripcion = Prescripcion(consulta_id=consulta_id, medicamento=medicamento, dosis=dosis)
    db.add(prescripcion)
    db.commit()
    return {"message": "Prescripción creada"}