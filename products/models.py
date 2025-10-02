from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField(null=True,blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    is_main = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image of {self.product.name}'


class ProductVariant(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]

    MATERIAL_CHOICES = [
        ('Cotton', 'Cotton'),
        ('Polyester', 'Polyester'),
        ('Silk', 'Silk'),
        ('Linen', 'Linen'),
        ('Wool', 'Wool'),
        ('Leather', 'Leather'),
        ('Nylon', 'Nylon'),
        ('Other', 'Other'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.size}/{self.material}/{self.color}"