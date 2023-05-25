from django.core.management.base import BaseCommand

from ganancias.models import Concepto
from ganancias.tablas.conceptos import CONCEPTOS


class Command(BaseCommand):
    help = 'Completar los conceptos en la base de datos'

    def handle(self, *args, **options):
        Concepto.objects.all().delete()

        for concepto in CONCEPTOS:
            if Concepto.objects.filter(name=concepto).count() == 0:
                print(f'Creando concepto {concepto}')
                print(CONCEPTOS[concepto], '!!!!!!!!!!!!')
                Concepto.objects.create(name=concepto, **CONCEPTOS[concepto])
                self.stdout.write(self.style.SUCCESS(f'Concepto {concepto} agregado'))
            else:
                self.stdout.write(self.style.SUCCESS(f'{concepto} sin cambios'))
