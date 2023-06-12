from django.db import models

from deducciones.models import Deduccion
from empresa.models import Empleado
from f1357.models import F1357Field


HABITUALIDAD = [
    ('HA', 'Habitual'),
    ('NH', 'No Habitual'),
]

PERIODICIDAD = [
    ('AN', 'Anual'),
    ('ME', 'Mensual'),
]

TIPO_CONCEPTO = [
    ('REM', 'Remunerativo'),
    ('NOREM', 'No Remunerativo'),
    ('APOR', 'Aporte'),
]

OTROS_CONCEPTOS = [
    ('SICOSS', 'Tope SICOSS'),
    ('EXBO', 'Exención Bono'),
]


class Concepto(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    long_name = models.CharField(max_length=120, verbose_name='Nombre Largo')
    tipo_concepto = models.CharField(max_length=5, choices=TIPO_CONCEPTO, default='REM')
    periodicidad = models.CharField(max_length=2, choices=PERIODICIDAD, default='ME')
    habitualidad = models.CharField(max_length=2, default='HA')
    exento = models.BooleanField(default=False)
    others = models.BooleanField(default=False, verbose_name='Otros Empleos')
    f1357field = models.ForeignKey(F1357Field, on_delete=models.SET_NULL, null=True, blank=True)
    extras = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.long_name

    class Meta:
        ordering = ['others', 'exento', 'tipo_concepto', 'name']


class Liquidacion(models.Model):
    nro_liq = models.PositiveSmallIntegerField(default=1)
    period = models.DateField()
    payday = models.DateField()

    def __str__(self) -> str:
        return f'{self.nro_liq}) {self.period.strftime("%Y/%m")} - {self.payday.strftime("%Y/%m/%d")}'

    class Meta:
        ordering = ['payday']
        verbose_name_plural = 'Liquidaciones'
        unique_together = [['nro_liq', 'period', 'payday']]


class ConceptoLiquidado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    liquidacion = models.ForeignKey(Liquidacion, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'{self.empleado.name} - {self.concepto.name} - {self.liquidacion} - $ {self.amount}'


class Aporte(models.Model):
    name = models.CharField(max_length=120, unique=True, primary_key=True, verbose_name='Nombre')
    long_name = models.CharField(max_length=120, verbose_name='Nombre Largo')
    descripcion = models.CharField(max_length=120, blank=True, null=True, verbose_name='Descripción')
    f1357field = models.ForeignKey(F1357Field, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.long_name


class AportesPorcentaje(models.Model):
    aporte = models.ForeignKey(Aporte, on_delete=models.CASCADE)
    valor = models.FloatField(default=0.0)
    validity_from = models.DateField(blank=True, null=True, verbose_name='Vigencia desde')
    validity_to = models.DateField(blank=True, null=True, verbose_name='Vigencia hasta')

    def __str__(self) -> str:
        return f'{self.aporte.name} - {self.validity_from.strftime("%Y/%m")} - $ {self.valor}'


class AporteLiquidado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    aporte = models.ForeignKey(Aporte, on_delete=models.CASCADE)
    liquidacion = models.ForeignKey(Liquidacion, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'{self.empleado.name} - {self.aporte.name} - {self.liquidacion} - $ {self.amount}'

    class Meta:
        ordering = ['liquidacion', 'empleado', 'aporte']
        verbose_name_plural = 'Aportes Liquidados'


class DeduccionEmpleado(models.Model):
    """ Deducción declaradas por empleado
    """
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    deduccion = models.ForeignKey(Deduccion, on_delete=models.CASCADE)
    validity_from = models.DateField(blank=True, null=True, verbose_name='Vigencia desde')
    validity_to = models.DateField(blank=True, null=True, verbose_name='Vigencia hasta')
    name = models.CharField(max_length=120, verbose_name='Nombre - Razón Social', null=True, blank=True)
    amount = models.FloatField(default=0.0, verbose_name='Importe')

    def __str__(self) -> str:
        resp = f'{self.empleado.name} - {self.deduccion.name} - {self.validity_from.strftime("%Y/%m")}'
        resp += f' - {self.validity_to.strftime("%Y/%m")} - $ {self.amount}'
        return resp

    class Meta:
        ordering = ['empleado', 'deduccion']
        verbose_name_plural = 'Deducciones Empleado'


class DeduccionPeriodo(models.Model):
    """ Deducción considerada en el período por empleado
    """
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    period = models.DateField()
    deduccion = models.ForeignKey(Deduccion, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'{self.empleado.name} - {self.period.strftime("%Y/%m")} - {self.deduccion} - $ {self.amount}'


class TablaArt94(models.Model):
    period = models.DateField(verbose_name='Periodo')
    from_value = models.FloatField(default=0.0, verbose_name='Desde')
    to_value = models.FloatField(default=0.0, verbose_name='Hasta')
    tax_percent = models.FloatField(default=0.0, verbose_name='Porcentaje')
    tax_fixed = models.FloatField(default=0.0, verbose_name='Fijo')

    def __str__(self) -> str:
        return f'{self.period.strftime("%Y/%m")} - {self.from_value} - {self.to_value} - {self.tax_percent} - {self.tax_fixed}'

    class Meta:
        ordering = ['-period', 'from_value']
        verbose_name_plural = 'Tabla Art. 94'


class OtrosConceptos(models.Model):
    """ Otros Conceptos - Tope SICOSS, Exención Bono
    """
    concepto = models.CharField(max_length=10, choices=OTROS_CONCEPTOS)
    validity_from = models.DateField(blank=True, null=True, verbose_name='Vigencia desde')
    validity_to = models.DateField(blank=True, null=True, verbose_name='Vigencia hasta')
    value = models.FloatField(default=0.0, verbose_name='Importe')

    def __str__(self) -> str:
        return f'{self.concepto} - {self.validity_from.strftime("%Y/%m")} - {self.validity_to.strftime("%Y/%m")}'

    class Meta:
        ordering = ['concepto']
        verbose_name_plural = 'Otros Conceptos'
