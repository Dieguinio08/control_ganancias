from datetime import date

from django.core.management.base import BaseCommand

from deducciones.models import Deduccion, TablaArt30, Tope, TopeValor
from deducciones.tablas.tablas import TABLA_ART_30, TOPES


class Command(BaseCommand):
    help = 'Completar todas las tablas del Impuesto a las Ganancias en la base de datos'

    def handle(self, *args, **options):
        self.tabla_art_30()
        self.topes()

    def topes(self):
        # TopeValor.objects.all().delete()

        for tope_year in TOPES:
            for i in range(1, 13):
                this_period = date(tope_year, i, 1)
                for tope in TOPES[tope_year]:
                    tope_obj = Tope.objects.get_or_create(name=tope)[0]
                    if TopeValor.objects.filter(tope=tope_obj, period=this_period).count() == 0:
                        is_yearly = TOPES[tope_year][tope].get('tipo', 'mensual') == 'anual'
                        divider = 1 if is_yearly else 12 / i
                        value = round(TOPES[tope_year][tope]['importe'] / divider, 2)
                        TopeValor.objects.create(period=this_period,
                                                 tope=tope_obj,
                                                 value=value)

                        msg = f'Tope {tope} para {this_period.strftime("%Y/%m")} agregado'
                        self.stdout.write(self.style.SUCCESS(msg))
                    else:
                        self.stdout.write(self.style.HTTP_INFO(f'Tope {tope} - {this_period.strftime("%Y/%m")} ya existe'))

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
