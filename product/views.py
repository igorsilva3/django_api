from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """ Um conjunto de visualizações para ver, editar e deletar instâncias de produtos """
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()