from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """ Um conjunto de visualizações para ver, editar e deletar instâncias de produtos """
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request):
    	queryset = Product.objects.all()
    	serializer = ProductSerializer(queryset, many=True)

    	return Response(serializer.data)