from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient   
from .models import CartItems
from carts.models import Carts
from products.models import Products
from customers.models import Customer
from categories.models import Categories

class TestCartItems(TestCase):
    def setUp(self):
        self.category1 = Categories.objects.create(
            name='category1',
            description='category1 description'
        )

        self.customer1 = Customer.objects.create(
            first_name='ash',
            last_name='kh',
            email='email@email.com',
            password='password',
            phone_number=1234567890,
            address='123, Main Street, Bangalore'
        )

        self.cart1 = Carts.objects.create(
            customer_id=self.customer1
        )

        self.product1 = Products.objects.create(
            name='product1',
            price=100,
            description='product1 description',
            stock_quantity=10,
            brand='brand1',
            category_id=self.category1
        )

        self.cartItems_data_1 = {
            'cart_id': self.cart1,
            'product_id': self.product1,
            'quantity': 1,
            'total_price': 100
        }

        self.cartItems_data_2 = {
            'cart_id': self.cart1,
            'product_id': self.product1,
            'quantity': 1,
            'total_price': 102
        }

        self.client = APIClient()
        self.cartItems1 = CartItems.objects.create(**self.cartItems_data_1)
        self.cartItems2 = CartItems.objects.create(**self.cartItems_data_2)
        self.url = reverse('cartItems-list')   

    def test_cartItems_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_carts_post(self):
        new_cartItems = {
            'cart_id': self.cart1.pk,
            'product_id': self.product1.pk,
            'quantity': 1,
            'total_price': 102
        }
        response = self.client.post(self.url, {'cartItems': [new_cartItems]}, format='json')
        self.assertEqual(response.status_code, 201)

    def test_carts_delete_all(self):
        url = reverse('cartItems-delete-all')
        self.assertEqual(CartItems.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CartItems.objects.count(), 0)
        self.assertEqual(response.data, {"message": "All cartItems have been deleted."})