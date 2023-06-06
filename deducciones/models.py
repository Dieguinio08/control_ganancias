import datetime
from django.conf import settings
from django.db import models

# Deducción 'AN' para deduccions a tomar en la anual o final
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


class Tope(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    descripcion = models.CharField(max_length=120, blank=True, null=True, verbose_name='Descripción')

    def __str__(self) -> str:
        return self.name


class TopeValor(models.Model):
    tope = models.ForeignKey(Tope, on_delete=models.CASCADE)
    period = models.DateField()
    value = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'{self.tope.name} - {self.period.strftime("%Y/%m")} - $ {self.value}'

    class Meta:
        ordering = ['-period', 'tope']
        unique_together = [['tope', 'period']]
        verbose_name_plural = 'Topes - Valores'


class Deduccion(models.Model):
    tipo = models.CharField(max_length=2, choices=DEDUCCION_TIPO, default='DE')
    codigo_siradig = models.CharField(max_length=20, verbose_name='Código Siradig')
    name = models.CharField(max_length=120, verbose_name='Nombre')
    periodicidad = models.CharField(max_length=2, choices=DEDUCCION_PERIODO, default='ME')
    tope = models.ForeignKey(Tope, on_delete=models.SET_NULL, blank=True, null=True)
    validity_from = models.DateField(default=datetime.datetime.strptime('2000-01-01', '%Y-%m-%d'),
                                     verbose_name='Vigencia desde')
    validity_to = models.DateField(default=datetime.datetime.strptime('2500-12-31', '%Y-%m-%d'), verbose_name='Vigencia hasta')

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


class RegAcceso(models.Model):
    reg_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.reg_user} - {self.fecha.strftime("%d/%m/%Y %H:%M")}'

    class Meta:
        ordering = ['-fecha']


class Registro(models.Model):
    id_reg = models.ForeignKey(RegAcceso, on_delete=models.CASCADE, related_name='registers')
    cuil = models.BigIntegerField()
    deduccion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    dato1 = models.CharField(max_length=50)
    dato2 = models.CharField(max_length=50, blank=True, null=True)
    porc = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id_reg.id} -{self.id_reg.reg_user} - {self.id_reg.fecha.strftime("%d/%m/%Y")} - {self.cuil}'


class TablaArt30(models.Model):
    deduccion = models.ForeignKey(Deduccion, on_delete=models.CASCADE)
    period = models.DateField(verbose_name='Periodo')
    value = models.FloatField(default=0.0, verbose_name='Importe')

    def __str__(self) -> str:
        return f'{self.deduccion} - {self.period.strftime("%Y/%m")} - $ {self.value}'

    class Meta:
        ordering = ['-period', 'deduccion']
        verbose_name_plural = 'Tabla Art. 30'


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
