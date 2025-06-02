from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import (
    configuracion_controller,
    paciente_controller,
    colaboradores_controller,
    citas_controller,
    consultas_controller,
    certificados_controller,
    contabilidad_controller,
    reportes_controller
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(configuracion_controller.router)
app.include_router(paciente_controller.router)
app.include_router(colaboradores_controller.router)
app.include_router(citas_controller.router)
app.include_router(consultas_controller.router)
app.include_router(certificados_controller.router)
app.include_router(contabilidad_controller.router)
app.include_router(reportes_controller.router)

@app.get("/")
def root():
    return {"message": "Sistema de Gestión Médica"}