from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import QuesoSerializer, MasaSerializer, TipoIngredienteSerializer, IngredienteSerializer, OtroProductoSerializer, MenuTradicionalSerializer
from .models import Queso, Masa, TipoIngrediente, Ingrediente, OtroProducto, MenuTradicional
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'tipo': ('exact',),
    }

    def get_queryset(self):
        tipos = self.request.query_params.get('tipos', [])
        if len(tipos)>0:
            lista_tipos = tipos.split(",")
            lista_tipos = [int(x) for x in lista_tipos]
            print(lista_tipos)
            return Ingrediente.objects.filter(disponible=True, tipo__id__in=lista_tipos)
        else:    
            return Ingrediente.objects.filter(disponible=True)
    
class OtroProductoListAPIView(ListAPIView):
    serializer_class = OtroProductoSerializer
    
    def get_queryset(self):
        return OtroProducto.objects.filter(disponible=True)
    
class MenuTradicionalListAPIView(ListAPIView):
    serializer_class = MenuTradicionalSerializer
    
    def get_queryset(self):
        return MenuTradicional.objects.filter(disponible=True).order_by('precio')
    

