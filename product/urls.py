from django.urls import path
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

app_name = 'product'

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls