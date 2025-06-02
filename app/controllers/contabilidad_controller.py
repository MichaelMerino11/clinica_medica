from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.contabilidad import PlanCuenta, Transaccion
from ..auth import verificar_token
from datetime import datetime

router = APIRouter(prefix="/contabilidad", tags=["Contabilidad"])

@router.post("/plan-cuentas")
def crear_cuenta(
    codigo: str, 
    nombre: str, 
    tipo: str, 
    db: Session = Depends(get_db),
    token: str = Depends(verificar_token)
):
    cuenta = PlanCuenta(codigo=codigo, nombre=nombre, tipo=tipo)
    db.add(cuenta)
    db.commit()
    return {"message": "Cuenta creada"}

@router.post("/transacciones")
def registrar_transaccion(
    monto: float, 
    tipo: str, 
    descripcion: str,
    cuenta_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(verificar_token)
):
    transaccion = Transaccion(
        monto=monto,
        tipo=tipo,
        descripcion=descripcion,
        fecha=datetime.now(),
        cuenta_id=cuenta_id
    )
    db.add(transaccion)
    db.commit()
    return {"message": "Transacción registrada"}