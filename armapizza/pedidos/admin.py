from django.contrib import admin
from .models import Pedido, Tamano, Pizza, IngredientesPizza, OtrosPedido
# Register your models here.
class TamanoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'factorial')


admin.site.register(Pedido)
admin.site.register(Tamano, TamanoAdmin)
admin.site.register(Pizza)
admin.site.register(IngredientesPizza)
admin.site.register(OtrosPedido)
