from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    description = models.CharField(max_length=120, blank=True, null=True, verbose_name='Descripción')
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class F1357Field(models.Model):
    name = models.CharField(max_length=60, unique=True, primary_key=True, verbose_name='Nombre')
    description = models.CharField(max_length=120, blank=True, null=True, verbose_name='Descripción')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
