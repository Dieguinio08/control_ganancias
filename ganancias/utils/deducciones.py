from datetime import date
import logging
from ganancias.exceptions import DeduccionIncrementadaException

from ganancias.models import DeduccionIncrementadaDetail, PeriodoDeduccionIncrementada


logger = logging.getLogger(__name__)


def get_deduccion_incrementada(remuneracion_base: float, period: date) -> float:
    deduccion_incrementada = 0.0

    my_period = PeriodoDeduccionIncrementada.objects.filter(
        validity_from__lte=period,
        validity_to__gte=period)

    if not my_period:
        logger.info(f'Período {period.strftime("%Y/%m")} no configurado')
        raise DeduccionIncrementadaException(f'Período {period.strftime("%Y/%m")} no configurado')

    my_row = DeduccionIncrementadaDetail.objects.filter(
        period=my_period.first(),
        from_value__lte=remuneracion_base,
        to_value__gte=remuneracion_base)

    if not my_row:
        logger.info(f'Período {period.strftime("%Y/%m")} - Remuneración Base {remuneracion_base} fuera rango')
        return 0.0

    deduccion_incrementada = my_row.first().value

    return deduccion_incrementada
