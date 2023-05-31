from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.forms.models import model_to_dict

from ganancias.validators import validate_cuil, validate_cuit, validate_name


CONSIDERACION_SAC = [
    ('AN', 'Anual'),
    ('JD', 'Junio - Diciembre'),
]

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


class Empresa(models.Model):
    name = models.CharField(max_length=120, verbose_name='Razon Social', validators=[validate_name])
    cuit = models.CharField(max_length=11, validators=[validate_cuit])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    take_sac = models.CharField(max_length=2, choices=CONSIDERACION_SAC, default='AN', verbose_name="Consideración SAC")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not hasattr(self, 'user'):
            user = get_current_user()
            if user and not user.pk:
                user = None

            self.user = user

        self.cuit = validate_cuit(self.cuit)
        self.name = validate_name(self.name)
        return super().save(force_insert, force_update, using, update_fields)

    def toJSON(self):
        item = model_to_dict(self)
        return item


class Empleado(models.Model):
    leg = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name='Nombre', validators=[validate_name])
    cuil = models.CharField(max_length=11, validators=[validate_cuil])
    jubilado = models.BooleanField(default=False)
    zona_patagonica = models.BooleanField(default=False, verbose_name="Zona Patagónica")
    fecha_baja = models.DateField(blank=True, null=True, verbose_name='Fecha de Baja')
    tope_35_anual = models.BooleanField(default=True, verbose_name="Tope Límite 35% Liq. Anual")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.empresa.name} - L.{self.leg}: {self.name}'

    def toJSON(self):
        item = model_to_dict(self)
        item['empresa'] = self.empresa.name
        return item

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.cuil = validate_cuil(self.cuil)
        self.name = validate_name(self.name)
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['empresa__name', 'leg']
        unique_together = (('leg', 'empresa'),)


class Concepto(models.Model):
    tipo_concepto = models.CharField(max_length=5, choices=TIPO_CONCEPTO, default='REM')
    periodicidad = models.CharField(max_length=2, choices=PERIODICIDAD, default='ME')
    name = models.CharField(max_length=100, verbose_name='Nombre', null=True, blank=True)
    habitualidad = models.CharField(max_length=2, default='HA')
    exento = models.BooleanField(default=False)
    others = models.BooleanField(default=False, verbose_name='Otros Empleos')
    extras = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['others', 'exento', 'tipo_concepto', 'name']


class Liquidacion(models.Model):
    period = models.DateField()
    payday = models.DateField()

    def __str__(self) -> str:
        return f'{self.period.strftime("%Y/%m")} - {self.payday.strftime("%Y/%m/%d")}'

    class Meta:
        ordering = ['payday']
        verbose_name_plural = 'Liquidaciones'
        unique_together = [['period', 'payday']]


class ConceptoLiquidado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)
    importe = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'{self.empleado.name} - {self.concepto.name} - $ {self.importe}'


class Aportes(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    descripcion = models.CharField(max_length=120, blank=True, null=True, verbose_name='Descripción')


class AportesPorcentaje(models.Model):
    aporte = models.ForeignKey(Aportes, on_delete=models.CASCADE)
    valor = models.FloatField(default=0.0)
    validity_from = models.DateField(blank=True, null=True, verbose_name='Vigencia desde')
    validity_to = models.DateField(blank=True, null=True, verbose_name='Vigencia hasta')

    def __str__(self) -> str:
        return f'{self.aporte.name} - {self.validity_from.strftime("%Y/%m")} - $ {self.valor}'


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


class PeriodoDeduccionIncrementada(models.Model):
    validity_from = models.DateField(blank=True, null=True, verbose_name='Vigencia desde')
    validity_to = models.DateField(blank=True, null=True, verbose_name='Vigencia hasta')
    sac_exento_limit = models.FloatField(default=0.0, verbose_name='Importe')

    def __str__(self) -> str:
        return f'{self.validity_from.strftime("%Y/%m")} - {self.validity_to.strftime("%Y/%m")}'

    class Meta:
        ordering = ['-validity_from']
        unique_together = [['validity_from', 'validity_to']]
        verbose_name_plural = 'Periodo Deducción Incrementada'


class DeduccionIncrementadaDetail(models.Model):
    period = models.ForeignKey(PeriodoDeduccionIncrementada, on_delete=models.CASCADE, verbose_name='Periodo')
    from_value = models.FloatField(default=0.0, verbose_name='Desde')
    to_value = models.FloatField(default=0.0, verbose_name='Hasta')
    value = models.FloatField(default=0.0, verbose_name='Importe')

    def __str__(self) -> str:
        return f'{self.period} - $ {self.from_value} - $ {self.value}'

    class Meta:
        ordering = ['period', 'value']
        verbose_name_plural = 'Detalle Deducción Incrementada'


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
