from datetime import date

from django.core.management.base import BaseCommand

from deducciones.models import Deduccion, TablaArt30
from deducciones.tablas.tablas import TABLA_ART_30


class Command(BaseCommand):
    help = 'Completar todas las tablas del Impuesto a las Ganancias en la base de datos'

    def handle(self, *args, **options):
        self.tabla_art_30()

    def tabla_art_30(self):
        # TablaArt30.objects.all().delete()

        for tabla in TABLA_ART_30:
            for i in range(1, 13):
                this_period = date(tabla, i, 1)
                for ded in TABLA_ART_30[tabla]:
                    deduccion = TABLA_ART_30[tabla][ded]
                    tipo_ded = Deduccion.get_tipo_code(deduccion['tipo'])
                    this_deduccion = Deduccion.objects.get(tipo=tipo_ded, codigo_siradig=deduccion['codigo'])
                    if TablaArt30.objects.filter(deduccion=this_deduccion, period=this_period).count() == 0:
                        value = round(deduccion['importe'] / 12 * i, 2)
                        TablaArt30.objects.create(period=this_period,
                                                  deduccion=this_deduccion,
                                                  value=value)

                        msg = f'Deduccion {ded} para {this_period.strftime("%Y/%m")} agregado'
                        self.stdout.write(self.style.SUCCESS(msg))
                    else:
                        self.stdout.write(self.style.HTTP_INFO(f'Deduccion {ded} - {this_period.strftime("%Y/%m")} ya existe'))
