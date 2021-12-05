from rest_framework import serializers
from .models import Portada

class PortadaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Portada
        fields = '__all__'