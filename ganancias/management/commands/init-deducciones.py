from django.core.management.base import BaseCommand

from ganancias.models import Deduccion
from ganancias.tablas.deducciones import DEDUCCIONES, DEDUCCIONES_ANUALES


class Command(BaseCommand):
    help = 'Completar las deducciones en la base de datos'
    # deduc_to_delete = Deduccion.objects.all()
    # deduc_to_delete.delete()

    def handle(self, *args, **options):
        for deduccion in DEDUCCIONES:
            ded_tipo = Deduccion.get_tipo_code(deduccion)
            for ded_cod, ded_name in DEDUCCIONES[deduccion].items():
                if Deduccion.objects.filter(tipo=ded_tipo, codigo_siradig=ded_cod).count() == 0:
                    if DEDUCCIONES_ANUALES.get(deduccion) and DEDUCCIONES_ANUALES.get(deduccion).get(ded_cod):
                        Deduccion.objects.create(tipo=ded_tipo, codigo_siradig=ded_cod, name=ded_name, periodicidad='AN')
                    else:
                        Deduccion.objects.create(tipo=ded_tipo, codigo_siradig=ded_cod, name=ded_name)
                    self.stdout.write(self.style.SUCCESS(f'Deduccion {ded_name} agregada'))
                else:
                    # Actualizar el nombre
                    deduccion = Deduccion.objects.get(tipo=ded_tipo, codigo_siradig=ded_cod)
                    if deduccion.name != ded_name:
                        self.stdout.write(self.style.WARNING(f'Actualizando pais {ded_name}'))
                        deduccion.name = ded_name
                        deduccion.save()
                    else:
                        self.stdout.write(self.style.SUCCESS(f'{ded_name} sin cambios'))
