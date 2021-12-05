from django.db import models
from django.conf import settings
from productos.models import Masa, Queso, Ingrediente, OtroProducto, MenuTradicional
# Create your models here.

class Pedido(models.Model):
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    direccion = models.CharField(max_length=250)
    valor_total = models.IntegerField()
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.direccion} Total: ${self.valor_total}"
    
class Tamano(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    factorial = models.FloatField()
    precio_base = models.IntegerField(default=10000)
    

    def __str__(self):
        return self.nombre

class Pizza(models.Model):
    
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    masa = models.ForeignKey(Masa, on_delete=models.CASCADE)
    queso = models.ForeignKey(Queso, on_delete=models.CASCADE)
    extra_queso = models.BooleanField(default=False)
    mitad_mitad = models.BooleanField(default=False)
    precio = models.IntegerField()
    cantidad = models.IntegerField(default=1)
    tamano = models.ForeignKey(Tamano, on_delete=models.CASCADE)

    def __str__(self):
        return self.pedido

class IngredientesPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    primera_mitad = models.BooleanField(default=True)

class OtrosPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(OtroProducto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=1)

class PizzaTradicional(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    opcion = models.ForeignKey(MenuTradicional, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Pizzas Tradicionales"

    def __str__(self):
        return self.pizza