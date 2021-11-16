from rest_framework import serializers
from .models import Pedido, Tamano, Pizza, IngredientesPizza, OtrosPedido

class PedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pedido
        fields = '__all__'
        
class TamanoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tamano
        fields = '__all__'
        
class PizzaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pizza
        fields = '__all__'
        
class IngredientesPizzaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IngredientesPizza
        fields = '__all__'
        
class OtrosPedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OtrosPedido
        fields = '__all__'