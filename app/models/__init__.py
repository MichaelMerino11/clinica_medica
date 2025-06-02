from sqlalchemy import ForeignKey  # Añadir esta línea
from .configuracion import Usuario, ParametroGeneral
from .contabilidad import PlanCuenta, Transaccion, Comprobante
from .paciente import Paciente, FacturacionTerceros
from .colaboradores import Medico, Colaborador
from .citas import Cita
from .consultas import Consulta, Prescripcion, OrdenMedica
from .certificados import Certificado
from .reportes import Reporte

__all__ = [
    'Usuario', 'ParametroGeneral',
    'PlanCuenta', 'Transaccion', 'Comprobante',
    'Paciente', 'FacturacionTerceros',
    'Medico', 'Colaborador',
    'Cita',
    'Consulta', 'Prescripcion', 'OrdenMedica',
    'Certificado',
    'Reporte',
    'ForeignKey'  # Añadir esto si se usa directamente desde aquí
]