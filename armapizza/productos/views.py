from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import QuesoSerializer, MasaSerializer, TipoIngredienteSerializer, IngredienteSerializer, OtroProductoSerializer
from .models import Queso, Masa, TipoIngrediente, Ingrediente, OtroProducto
# Create your views here.

class QuesosListAPIView(ListAPIView):
    serializer_class = QuesoSerializer
    
    def get_queryset(self):   
        return Queso.objects.filter(disponible=True)

class MasaListAPIView(ListAPIView):
    serializer_class = MasaSerializer
    
    def get_queryset(self):
        return Masa.objects.filter(disponible=True)

class TipoIngredienteListAPIView(ListAPIView):
    serializer_class = TipoIngredienteSerializer
    
    def get_queryset(self): 
        return TipoIngrediente.objects.all()
    
class IngredienteListAPIView(ListAPIView):
    serializer_class = IngredienteSerializer
    
    def get_queryset(self):
        return Ingrediente.objects.filter(disponible=True)
    
class OtroProductoListAPIView(ListAPIView):
    serializer_class = OtroProductoSerializer
    
    def get_queryset(self):
        return OtroProducto.objects.filter(disponible=True)
    

