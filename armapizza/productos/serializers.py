from rest_framework import serializers
from .models import Queso, Masa, TipoIngrediente, Ingrediente, OtroProducto, MenuTradicional

class QuesoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Queso
        fields = '__all__'

class MasaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Masa
        fields = '__all__'

class TipoIngredienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoIngrediente
        fields = '__all__'

class IngredienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingrediente
        fields = '__all__'

class OtroProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OtroProducto
        fields = '__all__'

class MenuTradicionalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenuTradicional
        fields = '__all__'
