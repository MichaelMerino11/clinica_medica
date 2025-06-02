from app.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

class PlanCuenta(Base):
    __tablename__ = "plan_cuentas"
    id = Column(Integer, primary_key=True)
    codigo = Column(String(20), unique=True)  # Ej: "1.1.01"
    nombre = Column(String(100))
    tipo = Column(String(20))  # "Activo", "Pasivo", "Ingreso", "Gasto"

class Transaccion(Base):
    __tablename__ = "transacciones"
    id = Column(Integer, primary_key=True)
    monto = Column(Float)
    tipo = Column(String(10))  # "INGRESO" o "EGRESO"
    descripcion = Column(String(200))
    fecha = Column(DateTime)
    cuenta_id = Column(Integer, ForeignKey("plan_cuentas.id"))