from fastapi import FastAPI
from .database import Base, engine
from .controllers import (
    configuracion_controller,
    paciente_controller,
    contabilidad_controller,
    colaboradores_controller,
    citas_controller,
    consultas_controller
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(configuracion_controller.router)
app.include_router(paciente_controller.router)
app.include_router(contabilidad_controller.router)
app.include_router(colaboradores_controller.router)
app.include_router(citas_controller.router)
app.include_router(consultas_controller.router)


@app.get("/")
def root():
    return {"message": "Sistema de Gestión Médica"}