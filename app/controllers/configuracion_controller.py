from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.configuracion_service import ConfiguracionService
from ..database import get_db

router = APIRouter(prefix="/configuracion", tags=["Configuración"])

@router.post("/usuarios")
def crear_usuario(email: str, password: str, perfil: str, db: Session = Depends(get_db)):
    service = ConfiguracionService(db)
    return service.crear_usuario(email, password, perfil)