from datetime import date
import logging
from ganancias.exceptions import GananciaNoCalculadaException

from ganancias.models import TablaArt94


logger = logging.getLogger(__name__)


def get_clean_name(name: str) -> str:
    """ Limpia el nombre de un concepto para que asignarse como primary key u otros usos
    """
    return name.replace(' ', '_').lower()


def get_impuesto_determinado(gnsi: float, period: date) -> float:
    impuesto_determinado = 0.0

    my_row = TablaArt94.objects.filter(
        period=period,
        from_value__lte=gnsi,
        to_value__gte=gnsi)

    if not my_row:
        logger.info(f'Ganancia {gnsi} no encontrada en la tabla del Art. 94 para el periodo {period.strftime("%Y/%m")}')
        raise GananciaNoCalculadaException(f'Ganancia {gnsi} no encontrada en la tabla del Art. 94')

    my_row = my_row.first()
    impuesto_determinado = my_row.tax_fixed + (gnsi - my_row.from_value) * my_row.tax_percent / 100

    return impuesto_determinado


def collect_period():
    """
    Recolecta todos los conceptos, aportes y deducciones de los empleados y los asigna a un periodo
    """
    pass
