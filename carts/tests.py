from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Carts
from .serializers import CartsSerializer
from customers.models import Customer

class CartsTestCase(TestCase):
    def setUp(self):
        self.customer1 = Customer.objects.create(
            first_name='ash',
            last_name='kh',
            email='email@email.com',
            password='password',
            phone_number=1234567890,
            address='123, Main Street, Bangalore'
        )

        self.carts_data_1 = {
            'customer_id': self.customer1,
        }

        self.carts_data_2 = {
            'customer_id': self.customer1,
        }

        self.client = APIClient()
        self.carts1 = Carts.objects.create(**self.carts_data_1)
        self.carts2 = Carts.objects.create(**self.carts_data_2)
        self.url = reverse('carts-list')       


    def test_carts_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_carts_post(self):
        new_carts = {
            'customer_id': self.customer1.pk,
        }
        response = self.client.post(self.url, {'carts': [new_carts]}, format='json')
        self.assertEqual(response.status_code, 201)

    def test_carts_delete_all(self):
        url = reverse('carts-delete-all')
        self.assertEqual(Carts.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Carts.objects.count(), 0)
        self.assertEqual(response.data, {"message": "All carts have been deleted."})
