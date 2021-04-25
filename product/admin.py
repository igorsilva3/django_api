from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_date', 'updated_date')
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)