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



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'is_main']



class ProducVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['size','material','color']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)       
    person = PersonSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    variants = ProducVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
