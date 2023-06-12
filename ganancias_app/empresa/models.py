from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.forms.models import model_to_dict

from empresa.validators import validate_cuil, validate_cuit, validate_name


CONSIDERACION_SAC = [
    ('AN', 'Anual'),
    ('JD', 'Junio - Diciembre'),
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
