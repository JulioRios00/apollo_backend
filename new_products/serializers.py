from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'color', 'category_display', 'price', 'promotional_price']
        read_only_fields = ['promotional_price']
    def get_category_display(self, obj):
        return obj.get_category_display()