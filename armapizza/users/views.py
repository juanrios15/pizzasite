from .models import Portada
from .serializers import PortadaSerializer

from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
class PortadaListAPIView(ListAPIView):
    serializer_class = PortadaSerializer
    
    def get_queryset(self):   
        return Portada.objects.order_by('orden')[:3]