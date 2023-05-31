from datetime import date
import logging
from deducciones.exceptions import DeduccionInexistenteException, DeduccionPeriodoException

from deducciones.models import Deduccion, TablaArt30, TopeValor


logger = logging.getLogger(__name__)


def get_toped_value(deduccion: Deduccion, period: date, amount: float) -> float:
    """Obtiene el valor de la deducción controlando el tope

    Args:
        deduccion (Deduccion): Deducción a controlar
        period (date): Período a controlar
        amount (float): En el caso de deducciones donde se informa valor

    Returns:
        float: Valor de la deducción a considerar
    """
    deduccion_value = 0.0
    if deduccion.tope:
        tope_value = TopeValor.objects.filter(
            tope=deduccion.tope,
            period=period)

        if tope_value:
            deduccion_value = min(amount, tope_value.first().value)
        else:
            deduccion_value = amount
    else:
        deduccion_value = amount

    return deduccion_value


def get_deduccion_periodo(deduccion_tipo: str, codigo_siradig: str, period: date, amount: float = 0.0) -> float:
    """Obtiene el valor de la deducción para el período indicado

    Args:
        deduccion_tipo (str): Tipo de Deducción
        codigo_siradig (str): Código Siradig, en el caso de subtipo, el formato es tt-sb
        period (date): Período a controlar
        amount (float): En el caso de deducciones donde se informa valor

    Raises:
        DeduccionInexistenteException: Deducción no configurada
        DeduccionPeriodoException: Deducción no configurada para este período o sin vigencia

    Returns:
        float: Valor de la deducción a considerar
    """
    deduccion = 0.0

    my_deduccion = Deduccion.objects.filter(
        tipo=deduccion_tipo,
        codigo_siradig=codigo_siradig)

    if not my_deduccion:
        logger.info(f'Deduccion {deduccion_tipo} - {codigo_siradig} no configurada')
        raise DeduccionInexistenteException(f'Deduccion {deduccion_tipo} - {codigo_siradig} no configurada')

    my_deduccion_period = my_deduccion.filter(
        validity_from__lte=period,
        validity_to__gte=period)

    if not my_deduccion_period:
        logger.info(f'Deduccion {deduccion_tipo} - {codigo_siradig} no configurada para el período {period.strftime("%Y/%m")}')
        msg = f'Deduccion {deduccion_tipo} - {codigo_siradig} no configurada para el período {period.strftime("%Y/%m")}'
        raise DeduccionPeriodoException(msg)

    # Las opciones de deducciones son:
    # - Art. 30 -> Retornar el valor de tabla
    # - Valor -> Retornar el valor de tabla luego del control del tope

    # Deducción Art. 30
    deduccion_art_30 = TablaArt30.objects.filter(
        deduccion=my_deduccion_period.first(),
        period=period)

    if deduccion_art_30:
        deduccion = deduccion_art_30.first().value
    else:
        deduccion = get_toped_value(my_deduccion_period.first(), period, amount)

    return deduccion
