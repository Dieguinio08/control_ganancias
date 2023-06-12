from django.contrib import admin

from deducciones.models import (Deduccion, DeduccionIncrementadaDetail, TablaArt30,
                                PeriodoDeduccionIncrementada, Tope, TopeValor)


admin.site.register(PeriodoDeduccionIncrementada)
admin.site.register(Tope)


@admin.register(Deduccion)
class DeduccionAdmin(admin.ModelAdmin):
    list_display = ("name", "tipo", "codigo_siradig", "periodicidad")
    list_filter = ("tipo",)
    list_per_page = 30


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


@admin.register(DeduccionIncrementadaDetail)
class DeduccionIncrementadaDetailAdmin(admin.ModelAdmin):
    list_display = ("period", "desde", "hasta", "value")
    list_filter = ("period", )
    list_per_page = 30

    @admin.display(empty_value='unknown')
    def desde(self, obj):
        return f'$ {"%.2f" % round(obj.from_value, 2)}'

    @admin.display(empty_value='unknown')
    def hasta(self, obj):
        return f'$ {"%.2f" % round(obj.to_value, 2)}'
