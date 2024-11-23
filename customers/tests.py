from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer

class CustomerTests(TestCase):
    def setUp(self):
        self.customer_data_1 = {
            'customer_id': '132',
            'first_name': 'ash',
            'last_name': "ka",
            "email": "email@email.com",
            "password": "324",
            "phone_number": 123,
            "address": "Beacon St"
        }
        self.customer_data_2 = {
            'customer_id': '1321',
            'first_name': 'ash',
            'last_name': "ka",
            "email": "email@email.com",
            "password": "3244",
            "phone_number": 123,
            "address": "Beacon St"
        }

        self.client = APIClient()
        self.customer1 = Customer.objects.create(**self.customer_data_1)
        self.customer2 = Customer.objects.create(**self.customer_data_2)
        self.url = reverse('customer-list')

    def test_get_customers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_customers(self):
        new_customers = [
            {
                'customer_id': '13277',
                'first_name': 'ash',
                'last_name': "ka",
                "email": "email@email.com",
                "password": "324",
                "phone_number": 123,
                "address": "Beacon St"
            },
            {   
                'customer_id': '13298',
                'first_name': 'ash',
                'last_name': "ka",
                "email": "email@email.com",
                "password": "324",
                "phone_number": 123,
                "address": "Beacon St"
            }
        ]

        response = self.client.post(self.url, {'customers': new_customers}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_customers(self):
        new_customers = [
            {
                'customer_id': '13277',
                'first_name': 'ash',
                'last_name': "ka",
                "email": "email@email.com",
                "password": "324",
                "phone_number": 123,
                "address": "Beacon St"
            },
            {   
                'customer_id': '13298',
                'first_name': 'ash',
                'last_name': "ka",
                "email": "email@email.com",
                "password": "324",
                "phone_number": 123,
                "address": "Beacon St"
            }
        ]

        response = self.client.post(self.url, {'customers': new_customers}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_delete_all_customers(self):
        url = reverse('customer-delete-all')
        self.assertEqual(Customer.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.count(), 0)
        self.assertEqual(response.data['message'], 'All customers have been deleted.')

    def test_delete_customer_by_id(self):
        url = reverse('customer-delete-by-id', args=[self.customer1.pk])
        self.assertEqual(Customer.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(response.data['message'], f"Customer with ID {self.customer1.pk} has been deleted.")
        self.assertFalse(Customer.objects.filter(pk=self.customer1.pk).exists())

    def test_get_customer_by_id(self):
        url = reverse('customer-get-by-id', args=[self.customer1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_id'], self.customer1.pk)
        self.assertEqual(response.data['first_name'], self.customer1.first_name)
        self.assertEqual(response.data['last_name'], self.customer1.last_name)
        self.assertEqual(response.data['email'], self.customer1.email)
        self.assertEqual(response.data['phone_number'], self.customer1.phone_number)
        self.assertEqual(response.data['address'], self.customer1.address)

