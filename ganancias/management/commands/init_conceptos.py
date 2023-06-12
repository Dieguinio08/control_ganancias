from django.core.management.base import BaseCommand

from f1357.models import F1357Field
from ganancias.models import Aporte, Concepto
from ganancias.tables.conceptos import APORTES, CONCEPTOS
from ganancias.utils.ganancias import get_clean_name


class Command(BaseCommand):
    help = 'Completar los conceptos en la base de datos'

    def handle(self, *args, **options):
        self.init_aportes()
        self.init_conceptos()

    def init_conceptos(self):
        # Concepto.objects.all().delete()
        for concepto in CONCEPTOS:
            concepto_name = get_clean_name(concepto)
            CONCEPTOS[concepto]['long_name'] = concepto

            if 'f1357field' in CONCEPTOS[concepto]:
                CONCEPTOS[concepto]['f1357field'] = F1357Field.objects.get(name=CONCEPTOS[concepto]['f1357field'])

            this_concepto = Concepto.objects.filter(name=concepto_name)
            if this_concepto.count() == 0:
                Concepto.objects.create(name=concepto_name, **CONCEPTOS[concepto])
                self.stdout.write(self.style.SUCCESS(f'Concepto {concepto} agregado'))
            else:
                if this_concepto[0].f1357field != CONCEPTOS[concepto].get('f1357field'):
                    this_concepto.update(**CONCEPTOS[concepto])
                    self.stdout.write(self.style.SUCCESS(f'{concepto} actualizado'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'{concepto} sin cambios'))

    def init_aportes(self):
        for aporte, values in APORTES.items():
            if 'f1357field' in APORTES[aporte]:
                values['f1357field'] = F1357Field.objects.get(name=values['f1357field'])

            this_aporte = Aporte.objects.filter(name=aporte)
            if this_aporte.count() == 0:
                Aporte.objects.create(name=aporte, **values)
                self.stdout.write(self.style.SUCCESS(f'Aporte {aporte} agregado'))
            else:
                if this_aporte[0].f1357field != values['f1357field'] or this_aporte[0].long_name != values['long_name']:
                    this_aporte.update(**values)
                    self.stdout.write(self.style.SUCCESS(f'{aporte} actualizado'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'{aporte} sin cambios'))
