from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.forms.models import model_to_dict

from ganancias.validators import validate_cuil, validate_cuit, validate_name

DEDUCCION_PERIODO = [
    ('AN', 'Anual'),
    ('ME', 'Mensual'),
]

DEDUCCION_TIPO = [
    ('DE', 'deduccion'),
    ('CF', 'cargaFamilia'),
    ('PC', 'retPerPago'),
    ('MA', 'manual'),
]

CONSIDERACION_SAC = [
    ('AN', 'Anual'),
    ('JD', 'Junio - Diciembre'),
]

HABITUALIDAD = [
    ('HA', 'Habitual'),
    ('NH', 'No Habitual'),
]

TIPO_CONCEPTO = [
    ('REM', 'Remunerativo'),
    ('NOREM', 'No Remunerativo'),
    ('APOR', 'Aporte'),
]


class Empresa(models.Model):
    name = models.CharField(max_length=120, verbose_name='Razon Social', validators=[validate_name])
    cuit = models.CharField(max_length=11, validators=[validate_cuit])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    take_sac = models.CharField(max_length=2, default='AN', verbose_name="Consideración SAC")
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
    periodicidad = models.CharField(max_length=2, choices=DEDUCCION_PERIODO, default='ME')
    name = models.CharField(max_length=100, verbose_name='Nombre', null=True, blank=True)
    habitualidad = models.CharField(max_length=2, default='HA')
    exento = models.BooleanField(default=False)
    others = models.BooleanField(default=False, verbose_name='Otros Empleos')
    extras = models.JSONField(default=dict)

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


class Tope(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    descripcion = models.CharField(max_length=120, blank=True, null=True, verbose_name='Descripción')

    def __str__(self) -> str:
        return self.name


class TopeValor(models.Model):
    tope = models.ForeignKey(Tope, on_delete=models.CASCADE)
    periodo = models.DateField()
    valor = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'{self.tope.name} - {self.periodo.strftime("%Y/%m")} - $ {self.valor}'


class Deduccion(models.Model):
    tipo = models.CharField(max_length=2, choices=DEDUCCION_TIPO, default='DE')
    codigo_siradig = models.CharField(max_length=20, verbose_name='Código Siradig')
    name = models.CharField(max_length=120, verbose_name='Nombre')
    periodicidad = models.CharField(max_length=2, choices=DEDUCCION_PERIODO, default='ME')
    tope = models.ForeignKey(Tope, on_delete=models.SET_NULL, blank=True, null=True)
    validity_from = models.DateField(blank=True, null=True, verbose_name='Vigencia desde')
    validity_to = models.DateField(blank=True, null=True, verbose_name='Vigencia hasta')

    class Meta:
        ordering = ['tipo', 'codigo_siradig']
        unique_together = [['tipo', 'codigo_siradig']]
        verbose_name_plural = 'Deducciones'

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_tipo_code(name_tipo: str) -> str:
        for tipo in DEDUCCION_TIPO:
            if tipo[1] == name_tipo:
                return tipo[0]
        # DE as default
        return "DE"


class Aportes(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    descripcion = models.CharField(max_length=120, blank=True, null=True, verbose_name='Descripción')


class AportesPorcentaje(models.Model):
    aporte = models.ForeignKey(Aportes, on_delete=models.CASCADE)
    valor = models.FloatField(default=0.0)
    validity_from = models.DateField(blank=True, null=True, verbose_name='Vigencia desde')
    validity_to = models.DateField(blank=True, null=True, verbose_name='Vigencia hasta')

    def __str__(self) -> str:
        return f'{self.aporte.name} - {self.periodo.strftime("%Y/%m")} - $ {self.valor}'
