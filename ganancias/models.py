from django.core.validators import MinLengthValidator
from django.db import models


DEDUCCION_PERIODO = [
    ('AN', 'Anual'),
    ('ME', 'Mensual'),
]

DEDUCCION_TIPO = [
    ('DG', 'Deducción General'),
    ('DP', 'Deducción Personal'),
]

DEDUCCION_TOPE = [
    (0, 'Sin Tope'),
    (1, r'Tope 5% Ganan 1'),
    (2, r'Tope 5% Ganan 2'),
]


class Empleado(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre', null=True, blank=True)
    cuil = models.CharField(max_length=11, validators=[MinLengthValidator(11)])

    def __str__(self) -> str:
        return f'{self.name} - {self.cuil}'

    class Meta:
        ordering = ['name']


class TipoConcepto(models.Model):
    code = models.CharField(primary_key=True, unique=True, max_length=20, verbose_name='Código Tipo')
    name = models.CharField(max_length=100, verbose_name='Tipo Concepto', null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Concepto(models.Model):
    tipo_concepto = models.ForeignKey(TipoConcepto, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Tipo Concepto', null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Liquidacion(models.Model):
    periodo = models.DateField()
    payday = models.DateField()

    def __str__(self) -> str:
        return f'{self.periodo.strftime("%Y/%m")} - {self.payday.strftime("%Y/%m/%d")}'

    class Meta:
        ordering = ['payday']
        verbose_name_plural = 'Liquidaciones'
        unique_together = [['periodo', 'payday']]


class ConceptoLiquidado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    importe = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'{self.empleado.name} - {self.concepto.name} - $ {self.importe}'


class Deduccion(models.Model):
    codigo_siradig = models.PositiveSmallIntegerField(primary_key=True, unique=True, verbose_name='Código Siradig')
    name = models.CharField(max_length=120, verbose_name='Nombre')
    tipo = models.CharField(max_length=2, choices=DEDUCCION_TIPO, default='DG')
    periodicidad = models.CharField(max_length=2, choices=DEDUCCION_PERIODO, default='ME')
    tope = models.PositiveSmallIntegerField(choices=DEDUCCION_TOPE, default=0)
    informa_en_unidad = models.BooleanField(default=False, verbose_name="¿Informa en unidad?")
    es_pago_ac = models.BooleanField(default=False, verbose_name="¿Es pago a cuenta?")

    class Meta:
        verbose_name_plural = 'Deducciones'

    def __str__(self) -> str:
        return self.name
