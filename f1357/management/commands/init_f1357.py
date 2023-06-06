from django.core.management.base import BaseCommand

from f1357.models import F1357Field, Group
from f1357.tables.schema import F1357_SCHEMA


class Command(BaseCommand):
    help = 'Completar las deducciones en la base de datos'
    Group.objects.all().delete()

    def handle(self, *args, **options):
        # Main Groups - for instance: 'remuneracion', 'deducciones'
        parent_id = None
        for main_item, values_0 in F1357_SCHEMA.items():
            parent_id_1, created = Group.objects.get_or_create(name=main_item, parent_id=parent_id)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Grupo {main_item} agregado'))

            if isinstance(values_0, list):
                for value_0 in values_0:
                    if F1357Field.objects.filter(name=value_0[0]).count() == 0:
                        F1357Field.objects.create(name=value_0[0], description=value_0[1], group=parent_id_1)
                        self.stdout.write(self.style.SUCCESS(f'Campo {value_0[0]} agregado'))
                continue

            # Sub Groups - for instance: 'agente_retencion', 'otros_empleos'
            for sub_item, values in F1357_SCHEMA[main_item].items():
                parent_id_2, created = Group.objects.get_or_create(name=sub_item, parent_id=parent_id_1)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Grupo {sub_item} agregado'))

                if isinstance(values, list):
                    for value in values:
                        if F1357Field.objects.filter(name=value[0]).count() == 0:
                            F1357Field.objects.create(name=value[0], description=value[1], group=parent_id_2)
                            self.stdout.write(self.style.SUCCESS(f'Campo {value[0]} agregado'))
                    continue

                # Sub Sub Groups - for instance: 'remuneracion_gravada', 'remuneracion_exenta'
                for field, values_2 in F1357_SCHEMA[main_item][sub_item].items():
                    parent_id_3, created = Group.objects.get_or_create(name=field, parent_id=parent_id_2)
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Grupo {sub_item} agregado'))
                    if isinstance(values_2, list):
                        for value_2 in values_2:
                            if F1357Field.objects.filter(name=value_2[0]).count() == 0:
                                F1357Field.objects.create(name=value_2[0], description=value_2[1], group=parent_id_3)
                                self.stdout.write(self.style.SUCCESS(f'Campo {value_2[0]} agregado'))
                    else:
                        self.stdout(self.style.ERROR('Error en el esquema de la tabla F1357'))
