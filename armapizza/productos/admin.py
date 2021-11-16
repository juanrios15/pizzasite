from django.contrib import admin
from .models import Queso, Masa, TipoIngrediente, Ingrediente, OtroProducto
# Register your models here.
class QuesoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')
    
class MasaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')

admin.site.register(Queso, QuesoAdmin)
admin.site.register(Masa, MasaAdmin)
admin.site.register(TipoIngrediente)
admin.site.register(Ingrediente)
admin.site.register(OtroProducto)