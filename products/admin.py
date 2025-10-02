from django.contrib import admin
from .models import Category,Person,Product,ProductImage

admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(ProductImage)