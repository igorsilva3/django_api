from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """ Cria um 'fornmulario' para manipular os dados no DB"""
    
    
    class Meta:

        model = Product
        fields = ('id', 'name', 'value')