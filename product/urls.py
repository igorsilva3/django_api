from django.urls import path
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

app_name = 'product'

# Cria o routeamento do app
router = DefaultRouter()

# Registra cada rota do app, baseado nos metodos das views
router.register(r'products', ProductViewSet, basename='product')

# Adiciona as rotas na urlpatterns do django
urlpatterns = router.urls