from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.paciente import Paciente, FacturacionTerceros
from ..auth import verificar_token
from ..services.paciente_service import PacienteService

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

@router.post("/")
def crear_paciente(
    nombre: str, 
    cedula: str, 
    telefono: str, 
    db: Session = Depends(get_db),
    token: str = Depends(verificar_token)
):
    service = PacienteService(db)
    return service.crear_paciente(nombre, cedula, telefono)

@router.post("/{paciente_id}/facturacion-terceros")
def agregar_facturacion_terceros(
    paciente_id: int,
    nombre: str,
    ruc: str,
    direccion: str,
    db: Session = Depends(get_db),
    token: str = Depends(verificar_token)
):
    facturacion = FacturacionTerceros(
        paciente_id=paciente_id,
        nombre=nombre,
        ruc=ruc,
        direccion=direccion
    )
    db.add(facturacion)
    db.commit()
    return {"message": "Datos de facturación añadidos"}