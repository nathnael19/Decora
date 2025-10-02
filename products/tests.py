from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Category, Person, ProductImage, ProductVariant

class ProductAPITest(APITestCase):
    def setUp(self):
        # Create a category
        self.category = Category.objects.create(name="Chairs")

        # Create a person
        self.person = Person.objects.create(
            name="John Doe",
            phone="1234567890",
            company="Furniture Co",
            address="123 Street",
            city="Addis Ababa"
        )

        # Create a product
        self.product = Product.objects.create(
            name="Wooden Chair",
            price=120.00,
            description="Comfortable chair",
            category=self.category,
            person=self.person,
            is_active=True
        )

        # Create variants
        self.variant1 = ProductVariant.objects.create(
            product=self.product,
            size="M",
            material="Wood",
            color="Brown"
        )
        self.variant2 = ProductVariant.objects.create(
            product=self.product,
            size="L",
            material="Wood",
            color="Black"
        )

        # Create product images
        self.image1 = ProductImage.objects.create(
            product=self.product,
            image="products/Screenshot_1-10-2025_0250_figmafreebie.com.jpeg",
            is_main=True
        )

    def test_list_products(self):
        url = reverse('product-list')  # assuming your router registered as 'product'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('images', response.data[0])
        self.assertIn('variants', response.data[0])
        self.assertIn('person', response.data[0])

    def test_retrieve_product(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('images', response.data)
        self.assertIn('variants', response.data)
        self.assertIn('person', response.data)

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            "name": "Dining Table",
            "price": 250.00,
            "description": "Large wooden table",
            "category": self.category.id,
            "person_id": self.person.id,  # 👈 must be the id, not Person object
            "is_active": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        url = reverse('product-detail', args=[self.product.id])
        data = {
            "name": "Updated Chair",
            "person_id": self.person.id  # 👈 use the id
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
