from django.db import models
from django.conf import settings
from productos.models import Masa, Queso, Ingrediente, OtroProducto
# Create your models here.

class Pedido(models.Model):
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    direccion = models.CharField(max_length=250)
    valor_total = models.IntegerField()
    email = models.CharField(max_length=80)
    celular = models.CharField(max_length=40)
    
class Tamano(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    factorial = models.FloatField()

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

class IngredientesPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    primera_mitad = models.BooleanField(default=True)

class OtrosPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(OtroProducto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=1)
    