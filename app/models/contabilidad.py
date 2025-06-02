from app.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

class PlanCuenta(Base):
    __tablename__ = "plan_cuentas"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True)
    nombre = Column(String(100))
    tipo = Column(String(20))  # ACTIVO, PASIVO, INGRESO, GASTO

class Transaccion(Base):
    __tablename__ = "transacciones"
    
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    monto = Column(Float)
    tipo = Column(String(10))  # INGRESO/EGRESO
    descripcion = Column(String(200))
    cuenta_id = Column(Integer, ForeignKey("plan_cuentas.id"))
    comprobante_id = Column(Integer, ForeignKey("comprobantes.id"))

class Comprobante(Base):
    __tablename__ = "comprobantes"
    
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(20), unique=True)
    fecha = Column(DateTime)
    monto_total = Column(Float)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))