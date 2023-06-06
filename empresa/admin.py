from django.contrib import admin

from empresa.models import Empleado, Empresa


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
