from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Geolocation
from .serializers import GeolocationSerializer

class GeolocationTests(TestCase):
    def setUp(self):
        self.geolocation1 = {
            'geolocation_zip_code_prefix': 111,
            'geolocation_lat': 42.122,
            'geolocation_lng': 54.66,
            "geolocation_city": "boston",
            "geolocation_state": "MA"

        }
        self.geolocation2 = {
            "geolocation_zip_code_prefix": 112,
            "geolocation_lat": 56.672,
            "geolocation_lng": 78.64,
            "geolocation_city": "boston",
            "geolocation_state": "MA"
        }

        self.client = APIClient()
        self.geolocation1 = Geolocation.objects.create(**self.geolocation1)
        self.geolocation2 = Geolocation.objects.create(**self.geolocation2)
        self.url = reverse('geolocation-list')

    def test_get_geolocations(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_geolocations(self):
        new_geolocations = {
            "geolocations": [
                {
                    "geolocation_zip_code_prefix": "1132431",
                    "geolocation_lat": 4223.122,
                    "geolocation_lng": 54324.66,
                    "geolocation_city": "boston",
                    "geolocation_state": "MA"
                },
                {
                    "geolocation_zip_code_prefix": "11345342",
                    "geolocation_lat": 56324.672,
                    "geolocation_lng": 78324.64,
                    "geolocation_city": "boston",
                    "geolocation_state": "MA"
                }
            ]
        }

        response = self.client.post(self.url, new_geolocations, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_all_geolocations(self):
        url = reverse('geolocation-delete-all')
        self.assertEqual(Geolocation.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Geolocation.objects.count(), 0)

    def test_delete_geolocations_by_id(self):
        url = reverse('geolocation-delete-by-id', args=[self.geolocation1.pk])
        self.assertEqual(Geolocation.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Geolocation.objects.count(), 1)
        self.assertFalse(Geolocation.objects.filter(pk=self.geolocation1.pk).exists())

    def test_get_geolocation_by_id(self):
        url = reverse('geolocation-get-by-id', args=[self.geolocation1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['geolocation_zip_code_prefix'], self.geolocation1.geolocation_zip_code_prefix)
        self.assertEqual(response.data['geolocation_lat'], self.geolocation1.geolocation_lat)
        self.assertEqual(response.data['geolocation_lng'], self.geolocation1.geolocation_lng)
        self.assertEqual(response.data['geolocation_city'], self.geolocation1.geolocation_city)
        self.assertEqual(response.data['geolocation_state'], self.geolocation1.geolocation_state)


