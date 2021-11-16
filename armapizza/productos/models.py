from django.db import models

# Create your models here.
class TipoIngrediente(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    tipo = models.ForeignKey(TipoIngrediente, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class Masa(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class Queso(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class OtroProducto(models.Model):
    
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre