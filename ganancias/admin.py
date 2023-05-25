from django.contrib import admin

from ganancias.models import Concepto, ConceptoLiquidado, Deduccion, Empleado, Empresa, TipoConcepto


admin.site.register(Concepto)
admin.site.register(ConceptoLiquidado)
admin.site.register(TipoConcepto)


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
