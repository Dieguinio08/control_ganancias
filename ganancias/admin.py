from django.contrib import admin

from ganancias.models import (Concepto, ConceptoLiquidado, Deduccion, Empleado,
                              Empresa, TablaArt30, TablaArt94, Tope, TopeValor)


admin.site.register(ConceptoLiquidado)
admin.site.register(Tope)


@admin.register(Concepto)
class ConceptoAdmin(admin.ModelAdmin):
    list_display = ("name", "tipo_concepto", "periodicidad", "habitualidad")
    list_filter = ("tipo_concepto", 'habitualidad')
    list_per_page = 30


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("leg", "name", "empresa", "cuil")
    list_filter = ("empresa",)
    list_per_page = 30


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("name", "cuit", "user", "view_created")
    list_filter = ("user", )
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def view_created(self, obj):
        return obj.created.strftime('%Y/%m/%d')


@admin.register(Deduccion)
class DeduccionAdmin(admin.ModelAdmin):
    list_display = ("name", "tipo", "codigo_siradig", "periodicidad")
    list_filter = ("tipo",)
    list_per_page = 30


@admin.register(TablaArt94)
class TablaArt94Admin(admin.ModelAdmin):
    list_display = ("periodo", "desde", "hasta", "porcentaje", "fijo")
    list_filter = ("period", )
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def periodo(self, obj):
        return obj.period.strftime('%Y/%m')

    @admin.display(empty_value='unknown')
    def desde(self, obj):
        return f'$ {"%.2f" % round(obj.from_value, 2)}'

    @admin.display(empty_value='unknown')
    def hasta(self, obj):
        return f'$ {"%.2f" % round(obj.to_value, 2)}'

    @admin.display(empty_value='unknown')
    def porcentaje(self, obj):
        return f'{round(obj.tax_percent)}%'

    @admin.display(empty_value='unknown')
    def fijo(self, obj):
        return f'$ {"%.2f" % round(obj.tax_fixed, 2)}'


@admin.register(TablaArt30)
class TablaArt30Admin(admin.ModelAdmin):
    list_display = ("periodo", "deduccion", "importe")
    list_filter = ("period", "deduccion")
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def periodo(self, obj):
        return obj.period.strftime('%Y/%m')

    @admin.display(empty_value='unknown')
    def importe(self, obj):
        return f'$ {"%.2f" % round(obj.value, 2)}'


@admin.register(TopeValor)
class TopeValorAdmin(admin.ModelAdmin):
    list_display = ("tope", "periodo", "value")
    list_filter = ("tope", 'period')
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def periodo(self, obj):
        return obj.period.strftime('%Y/%m')
