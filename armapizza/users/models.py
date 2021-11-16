from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
# Create your models here.


class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    slug = models.SlugField(default="",editable=False,max_length=150, blank=True, null=True)
    
    def save(self,*args, **kwargs):
        
        if not self.slug:
            
            self.slug = slugify(self.username)

        super(User,self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.username

class Portada(models.Model):

    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    seleccion = models.BooleanField(default=False)