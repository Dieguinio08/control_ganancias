from django.contrib import admin

from ganancias.models import Concepto, ConceptoLiquidado, Deduccion, Empleado, TipoConcepto


admin.site.register(Concepto)
admin.site.register(ConceptoLiquidado)
admin.site.register(Deduccion)
admin.site.register(Empleado)
admin.site.register(TipoConcepto)
