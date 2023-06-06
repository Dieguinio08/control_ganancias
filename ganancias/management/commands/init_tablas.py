from datetime import date, datetime

from django.core.management.base import BaseCommand

from ganancias.models import (DeduccionIncrementadaDetail, OtrosConceptos,
                              PeriodoDeduccionIncrementada, TablaArt94)
from ganancias.tables.tablas import (DEDUCCION_INCREMENTADA, TABLA_ART_94,
                                     TABLAS_OTROS_CONCEPTOS)


class Command(BaseCommand):
    help = 'Completar todas las tablas del Impuesto a las Ganancias en la base de datos'

    def handle(self, *args, **options):
        self.tabla_art_94()
        self.deduccion_incrementada()
        self.otros_conceptos()

    def otros_conceptos(self):
        # OtrosConceptos.objects.all().delete()

        for concepto in TABLAS_OTROS_CONCEPTOS:
            for period in TABLAS_OTROS_CONCEPTOS[concepto]:
                v_from = datetime.strptime(period[0], '%Y-%m-%d').date()
                v_to = datetime.strptime(period[1], '%Y-%m-%d').date()
                value = period[2]

                if OtrosConceptos.objects.filter(concepto=concepto,
                                                 validity_from=v_from).count() == 0:
                    OtrosConceptos.objects.create(concepto=concepto,
                                                  validity_from=v_from,
                                                  validity_to=v_to,
                                                  value=value)
                    msg = f'Tabla {concepto} - {period[0]} a {period[1]} agregada'
                    self.stdout.write(self.style.SUCCESS(msg))
                else:
                    this_concepto = OtrosConceptos.objects.get(concepto=concepto,
                                                               validity_from=v_from)

                    if this_concepto.value == float(value) and this_concepto.validity_to == v_to:
                        msg = f'Tabla {concepto} - {period[0]} a {period[1]} ya existe'
                        self.stdout.write(self.style.NOTICE(msg))
                    else:
                        this_concepto.value = value
                        this_concepto.validity_to = v_to
                        this_concepto.save()
                        msg = f'Tabla {concepto} - {period[0]} a {period[1]} actualizada'
                        self.stdout.write(self.style.WARNING(msg))

    def deduccion_incrementada(self):
        # PeriodoDeduccionIncrementada.objects.all().delete()

        for period in DEDUCCION_INCREMENTADA:
            v_from = datetime.strptime(period['vigencia_desde'], '%Y-%m-%d')
            v_to = datetime.strptime(period['vigencia_hasta'], '%Y-%m-%d')
            sac_exento_limit = period['sac_exento']

            period_obj = PeriodoDeduccionIncrementada.objects.get_or_create(validity_from=v_from,
                                                                            validity_to=v_to,
                                                                            sac_exento_limit=sac_exento_limit)[0]
            for i in range(len(period['deducciones']) - 1):
                # En la última linea la deduccion es $0, no la incluyo
                from_value = period['deducciones'][i][0] + 0.01
                to_value = period['deducciones'][i + 1][0]
                value = period['deducciones'][i][1]

                if DeduccionIncrementadaDetail.objects.filter(period=period_obj,
                                                              from_value=from_value).count() == 0:
                    DeduccionIncrementadaDetail.objects.create(period=period_obj,
                                                               from_value=from_value,
                                                               to_value=to_value,
                                                               value=value)
                    msg = f'Dedu {period_obj} - $ {"%.2f" % round(from_value, 2)} a $ {"%.2f" % round(to_value, 2)} agregada'
                    self.stdout.write(self.style.SUCCESS(msg))
                else:
                    msg = f'Dedu {period_obj} - $ {"%.2f" % round(from_value, 2)} a $ {"%.2f" % round(to_value, 2)} ya existe'
                    self.stdout.write(msg)

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
