from rest_framework import serializers
from .models import Product, Category,Person,ProductImage,ProductVariant



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"