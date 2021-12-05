from django.contrib import admin
from .models import Queso, Masa, TipoIngrediente, Ingrediente, OtroProducto, MenuTradicional
# Register your models here.
class QuesoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')
    
class MasaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')
    
class MenuTradicionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')

class OtroProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')

admin.site.register(Queso, QuesoAdmin)
admin.site.register(Masa, MasaAdmin)
admin.site.register(TipoIngrediente)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(OtroProducto, OtroProductoAdmin)
admin.site.register(MenuTradicional, MenuTradicionalAdmin)