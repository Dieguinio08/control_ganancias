from datetime import date

from django.core.management.base import BaseCommand

from ganancias.models import Deduccion, TablaArt30, TablaArt94, Tope, TopeValor
from ganancias.tablas.tablas import TABLA_ART_30, TABLA_ART_94, TOPES


class Command(BaseCommand):
    help = 'Completar todas las tablas del Impuesto a las Ganancias en la base de datos'

    def handle(self, *args, **options):
        # self.tabla_art_30()
        # self.tabla_art_94()
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

    def tabla_art_94(self):
        TablaArt94.objects.all().delete()
        self.stdout.write(self.style.NOTICE('TablaArt94 eliminada para cargarla nuevamente'))

        for tabla in TABLA_ART_94:
            for i in range(1, 13):
                this_period = date(tabla, i, 1)
                tax_fixed = 0
                for j in range(len(TABLA_ART_94[tabla])):
                    from_value = round(TABLA_ART_94[tabla][j][0] / 12 * i, 2)
                    to_value = 9999999999
                    if j + 1 < len(TABLA_ART_94[tabla]):
                        to_value = round(TABLA_ART_94[tabla][j + 1][0] / 12 * i, 2) - 0.01
                    TablaArt94.objects.create(period=this_period,
                                              from_value=from_value,
                                              to_value=to_value,
                                              tax_percent=TABLA_ART_94[tabla][j][1],
                                              tax_fixed=tax_fixed)
                    tax_fixed += (to_value - from_value + 0.01) * TABLA_ART_94[tabla][j][1] / 100
                    msg = f'Período {this_period.strftime("%Y/%m")} de {from_value} a {to_value} agregado'
                    self.stdout.write(self.style.SUCCESS(msg))
