from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Sellers
from geolocations.models import Geolocation
from geolocations.serializers import GeolocationSerializer

class SellerTests(TestCase):
    def setUp(self):
        self.geolocation_1 = Geolocation.objects.create(
            geolocation_zip_code_prefix=123, geolocation_lat = 23.33, geolocation_lng = 23.34, geolocation_city="boston",
            geolocation_state = 'MA'
        )

        self.geolocation_2 = Geolocation.objects.create(
            geolocation_zip_code_prefix=456, geolocation_lat = 27.31, geolocation_lng = 28.34, geolocation_city="boston",
            geolocation_state = 'MA'
        )

        self.seller_data_1 = {
            'seller_id': '132',
            'seller_zip_code_prefix': self.geolocation_1,
            'seller_state': 'MA',
            "seller_city": "boston"
        }

        self.seller_data_2 = {
            'seller_id': '1321',
            'seller_zip_code_prefix': self.geolocation_1,
            'seller_state': 'MA',
            'seller_city': "boston"
        }

        self.client = APIClient()
        Sellers.objects.create(**self.seller_data_1)
        Sellers.objects.create(**self.seller_data_2)
        self.url = reverse('seller-list')

    def test_get_sellers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_sellers(self):
        geolocation_data_2 = GeolocationSerializer(self.geolocation_2).data
        new_sellers = [
            {
                'seller_id': '1300222',
                'seller_zip_code_prefix': geolocation_data_2['geolocation_zip_code_prefix'],
                'seller_state': 'MA',
                'seller_city': "boston"
            },
            {   
                'seller_id': '1321222',
                'seller_zip_code_prefix': geolocation_data_2['geolocation_zip_code_prefix'],
                'seller_state': 'MA',
                'seller_city': "boston"
            }
        ]

        response = self.client.post(self.url, {'sellers': new_sellers}, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)