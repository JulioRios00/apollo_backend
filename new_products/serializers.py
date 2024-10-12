from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'color', 'category', 'price', 'promotional_price']
        read_only_fields = ['promotional_price']