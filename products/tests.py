from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Products
from categories.models import Categories
from categories.serializers import CategoriesSerializer

class ProductsTests(TestCase):
    def setUp(self):
        self.categories1 = Categories.objects.create(
            name="Food", description='Tastes good!'
        )

        self.categories2 = Categories.objects.create(
            name="Food1", description='Tastes good!1'
        )

        self.products_data_1 = {
            'product_id': '123',
            'name': 'Foodx',
            'description': 'Foodx',
            "price": 23.56,
            "stock_quantity": 34,
            "category_id": self.categories1,
            "brand": "Haldiram"
        }

        self.products_data_2 = {
            'product_id': '1366',
            'name': 'Foodex',
            'description': 'Foodx1',
            "price": 13.56,
            "stock_quantity": 32,
            "category_id": self.categories1,
            "brand": "Haldiram"
        }

        self.client = APIClient()
        self.products1 = Products.objects.create(**self.products_data_1)
        self.products2 = Products.objects.create(**self.products_data_2)
        self.url = reverse('products-list')

    def test_get_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_products(self):
        categories_data_2 = CategoriesSerializer(self.categories2).data
        new_products = [
            {
                'product_id': '13',
                'name': 'Foodex',
                'description': 'Foodx1',
                "price": 13.56,
                "stock_quantity": 32,
                "category_id": categories_data_2['id'],
                "brand": "Haldiram",
            },
            {   
                'product_id': '1356',
                'name': 'Foodexq',
                'description': 'Fooqdx1',
                "price": 13.56,
                "stock_quantity": 32,
                "category_id": categories_data_2['id'],
                "brand": "Haldiram"
            }
        ]

        response = self.client.post(self.url, {'products': new_products}, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_all_products(self):
        url = reverse('products-delete-all')
        self.assertEqual(Products.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Products.objects.count(), 0)
        self.assertEqual(response.data['message'], 'All products have been deleted.')

    def test_delete_sellers_by_id(self):
        url = reverse('products-delete-by-id', args=[self.products1.pk])
        self.assertEqual(Products.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Products.objects.count(), 1)
        self.assertEqual(response.data['message'], f"Products with ID {self.products1.pk} has been deleted.")
        self.assertFalse(Products.objects.filter(pk=self.products1.pk).exists())

    def test_get_sellers_by_id(self):
        url = reverse('products-get-by-id', args=[self.products1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_id'], self.products1.product_id)
        self.assertEqual(response.data['name'], self.products1.name)
        self.assertEqual(response.data['description'], self.products1.description)
        self.assertEqual(response.data['price'], self.products1.price)
        self.assertEqual(response.data['stock_quantity'], self.products1.stock_quantity)
        self.assertEqual(response.data['brand'], self.products1.brand)
        # self.assertEqual(response.data['created_at'], self.products1.created_at)




