from django.contrib import admin
from .models import Category,Person,Product,ProductImage,ProductVariant

admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)