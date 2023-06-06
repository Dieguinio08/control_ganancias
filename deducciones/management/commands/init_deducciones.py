from datetime import date

from django.core.management.base import BaseCommand

from deducciones.models import Deduccion, Tope, TopeValor
from deducciones.tables.deducciones import DEDUCCIONES, TOPES


class Command(BaseCommand):
    help = 'Completar las deducciones en la base de datos'
    # deduc_to_delete = Deduccion.objects.all()
    # deduc_to_delete.delete()

    def handle(self, *args, **options):
        self.topes()
        self.deducciones()

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

    def deducciones(self):
        for deduccion in DEDUCCIONES:
            ded_tipo = Deduccion.get_tipo_code(deduccion)
            for ded_cod, ded_name in DEDUCCIONES[deduccion].items():
                ded_args = {'name': ded_name} if ded_tipo != 'DE' else ded_name
                # Predeterminado todos los pagos a cuentas son anuales
                if ded_tipo == 'PC' and 'periodicidad' not in ded_args:
                    ded_args['periodicidad'] = 'AN'
                if 'tope' in ded_args:
                    ded_args['tope'] = Tope.objects.get(name=ded_args['tope'])
                if Deduccion.objects.filter(tipo=ded_tipo, codigo_siradig=ded_cod).count() == 0:
                    Deduccion.objects.create(tipo=ded_tipo, codigo_siradig=ded_cod, **ded_args)
                    self.stdout.write(self.style.SUCCESS(f'Deduccion {ded_args["name"]} agregada'))
                else:
                    # Actualizar el nombre
                    deduccion = Deduccion.objects.get(tipo=ded_tipo, codigo_siradig=ded_cod)
                    if deduccion.name != ded_args['name']:
                        self.stdout.write(self.style.WARNING(f'Actualizando deducción {ded_args["name"]}'))
                        deduccion.name = ded_args['name']
                        deduccion.save()
                    else:
                        self.stdout.write(self.style.SUCCESS(f'{ded_args["name"]} sin cambios'))
