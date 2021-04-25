from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('product/', views.ProductList.as_view(), name='product'),
]