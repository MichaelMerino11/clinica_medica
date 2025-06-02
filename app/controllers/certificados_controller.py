from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.certificados import Certificado
from ..auth import verificar_token

router = APIRouter(prefix="/certificados", tags=["Certificados"])

@router.post("/")
def emitir_certificado(consulta_id: int, contenido: str,
                      db: Session = Depends(get_db), token: str = Depends(verificar_token)):
    certificado = Certificado(consulta_id=consulta_id, contenido=contenido)
    db.add(certificado)
    db.commit()
    return {"message": "Certificado emitido", "id": certificado.id}