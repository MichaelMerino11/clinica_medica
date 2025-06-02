from fastapi import FastAPI
from app.controllers import configuracion_controller, paciente_controller
from app.database import Base, engine 

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(configuracion_controller.router)
app.include_router(paciente_controller.router)

@app.get("/")
def read_root():
    return {"message": "Sistema de Citas Médicas"}