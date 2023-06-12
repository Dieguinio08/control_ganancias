from django.contrib import admin

from ganancias.models import (Aporte, AporteLiquidado, Concepto, ConceptoLiquidado,
                              DeduccionEmpleado, Liquidacion, OtrosConceptos, TablaArt94)


admin.site.register(Aporte)
admin.site.register(OtrosConceptos)


@admin.register(Concepto)
class ConceptoAdmin(admin.ModelAdmin):
    list_display = ("long_name", "tipo_concepto", "periodicidad", "habitualidad")
    list_filter = ("tipo_concepto", 'habitualidad')
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


@admin.register(ConceptoLiquidado)
class ConceptoLiquidadoAdmin(admin.ModelAdmin):
    list_display = ("empleado", "concepto", "liquidacion", "importe")
    list_filter = ("empleado", "concepto")
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def importe(self, obj):
        return f'$ {"%.2f" % round(obj.amount, 2)}'


@admin.register(AporteLiquidado)
class AporteLiquidadoAdmin(admin.ModelAdmin):
    list_display = ("empleado", "aporte", "liquidacion", "importe")
    list_filter = ("empleado", "aporte")
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def importe(self, obj):
        return f'$ {"%.2f" % round(obj.from_value, 2)}'


@admin.register(DeduccionEmpleado)
class DeduccionEmpleadoAdmin(admin.ModelAdmin):
    list_display = ("empleado", "deduccion", "desde", "hasta", "importe")
    list_filter = ("empleado", "deduccion")
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def desde(self, obj):
        return obj.validity_from.strftime('%Y/%m')

    @admin.display(empty_value='unknown')
    def hasta(self, obj):
        return obj.validity_to.strftime('%Y/%m')

    @admin.display(empty_value='unknown')
    def importe(self, obj):
        return f'$ {"%.2f" % round(obj.amount, 2)}'


@admin.register(Liquidacion)
class LiquidacionAdmin(admin.ModelAdmin):
    list_display = ("nro_liq", "periodo", "fecha_pago")
    list_display_links = ("periodo", "fecha_pago")
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def periodo(self, obj):
        return obj.period.strftime('%Y/%m')

    @admin.display(empty_value='unknown')
    def fecha_pago(self, obj):
        return obj.payday.strftime('%Y/%m')
