from rest_framework import serializers
from .models import Product, Category,Person,ProductImage,ProductVariant



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name','phone','company','address','city']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"