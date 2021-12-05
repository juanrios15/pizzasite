from django.contrib import admin
from .models import Pedido, Tamano, Pizza, IngredientesPizza, OtrosPedido, PizzaTradicional
# Register your models here.
class TamanoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'factorial')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'direccion', 'valor_total', 'celular', 'email' )

class PizzaTradicionalAdmin(admin.ModelAdmin):
    list_display = ('pizza', 'opcion' )


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Tamano, TamanoAdmin)
admin.site.register(Pizza)
admin.site.register(IngredientesPizza)
admin.site.register(OtrosPedido)
admin.site.register(PizzaTradicional)
