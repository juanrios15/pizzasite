from django.shortcuts import render
from .models import Tamano
from .serializers import TamanoSerializer, PedidoSerializer, PizzaSerializer, IngredientesPizzaSerializer, OtrosPedidoSerializer

from rest_framework.generics import CreateAPIView, ListAPIView
# Create your views here.

class TamanosListAPIView(ListAPIView):
    serializer_class = TamanoSerializer
    
    def get_queryset(self):   
        return Tamano.objects.all()

class PedidoCreateAPIView(CreateAPIView):
    serializer_class = PedidoSerializer

class PizzaCreateAPIView(CreateAPIView):
    serializer_class = PizzaSerializer
    
class IngredientesPizzaCreateAPIView(CreateAPIView):
    serializer_class = IngredientesPizzaSerializer
    
class OtrosCreateAPIView(CreateAPIView):
    serializer_class = OtrosPedidoSerializer
