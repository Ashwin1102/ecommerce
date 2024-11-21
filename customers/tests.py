from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer
from geolocations.models import Geolocation
from geolocations.serializers import GeolocationSerializer

class CustomerTests(TestCase):
    def setUp(self):
        self.geolocation_1 = Geolocation.objects.create(
            geolocation_zip_code_prefix=123, geolocation_lat = 23.33, geolocation_lng = 23.34, geolocation_city="boston",
            geolocation_state = 'MA'
        )

        self.geolocation_2 = Geolocation.objects.create(
            geolocation_zip_code_prefix=456, geolocation_lat = 27.31, geolocation_lng = 28.34, geolocation_city="boston",
            geolocation_state = 'MA'
        )

        self.customer_data_1 = {
            'customer_id': '132',
            'customer_unique_id': '3242',
            'customer_zip_code_prefix': self.geolocation_1,
            "customer_city": "324",
            "customer_state": "43"

        }
        self.customer_data_2 = {
            "customer_id": "1321",
            "customer_unique_id": "32421",
            "customer_zip_code_prefix": self.geolocation_1,
            "customer_city": "3241",
            "customer_state": "431"
        }

        self.client = APIClient()
        self.customer1 = Customer.objects.create(**self.customer_data_1)
        self.customer2 = Customer.objects.create(**self.customer_data_2)
        self.url = reverse('customer-list')

    def test_get_customers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_customers(self):
        geolocation_data_2 = GeolocationSerializer(self.geolocation_2).data
        new_customers = [
            {
                "customer_id": "13256",
                "customer_unique_id": "3",
                "customer_zip_code_prefix": geolocation_data_2['geolocation_zip_code_prefix'],
                "customer_city": "3241",
                "customer_state": "431"
            },
            {   
                "customer_id": "13267",
                "customer_unique_id": "35",
                "customer_zip_code_prefix": geolocation_data_2['geolocation_zip_code_prefix'],
                "customer_city": "324",
                "customer_state": "31"
            }
        ]

        response = self.client.post(self.url, {'customers': new_customers}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_customers(self):
        geolocation_data_2 = GeolocationSerializer(self.geolocation_2).data
        new_customers = [
            {
                "customer_id": "13256",
                "customer_unique_id": "3",
                "customer_zip_code_prefix": geolocation_data_2['geolocation_zip_code_prefix'],
                "customer_city": "3241",
                "customer_state": "431"
            },
            {   
                "customer_id": "13267",
                "customer_unique_id": "35",
                "customer_zip_code_prefix": geolocation_data_2['geolocation_zip_code_prefix'],
                "customer_city": "324",
                "customer_state": "31"
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
        self.assertEqual(response.data['customer_unique_id'], self.customer1.customer_unique_id)
        self.assertEqual(response.data['customer_city'], self.customer1.customer_city)
        self.assertEqual(response.data['customer_state'], self.customer1.customer_state)

