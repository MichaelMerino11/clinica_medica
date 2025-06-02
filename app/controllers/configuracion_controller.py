from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.configuracion import Usuario
from ..schemas.token import Token
from ..auth import crear_token, verificar_token, get_usuario_actual
from ..services.configuracion_service import ConfiguracionService

router = APIRouter(prefix="/configuracion", tags=["Configuración"])

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    service = ConfiguracionService(db)
    usuario = service.autenticar_usuario(form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = crear_token(data={"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/usuarios")
def crear_usuario(
    email: str, 
    password: str, 
    perfil: str, 
    db: Session = Depends(get_db),
    usuario_actual: Usuario = Depends(get_usuario_actual)
):
    service = ConfiguracionService(db)
    return service.crear_usuario(email, password, perfil)

@router.get("/usuarios/me")
def leer_usuario_actual(usuario_actual: Usuario = Depends(get_usuario_actual)):
    return usuario_actual