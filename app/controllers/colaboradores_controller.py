from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.colaboradores import Medico, Colaborador
from ..auth import verificar_token

router = APIRouter(prefix="/colaboradores", tags=["Colaboradores"])

@router.post("/medicos")
def crear_medico(nombre: str, especialidad: str, usuario_id: int, 
                db: Session = Depends(get_db), token: str = Depends(verificar_token)):
    medico = Medico(nombre=nombre, especialidad=especialidad, usuario_id=usuario_id)
    db.add(medico)
    db.commit()
    return {"message": "Médico creado"}

@router.post("/colaboradores")
def crear_colaborador(nombre: str, rol: str, usuario_id: int,
                     db: Session = Depends(get_db), token: str = Depends(verificar_token)):
    colaborador = Colaborador(nombre=nombre, rol=rol, usuario_id=usuario_id)
    db.add(colaborador)
    db.commit()
    return {"message": "Colaborador creado"}