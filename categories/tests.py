from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Categories
from .serializers import CategoriesSerializer

class CategoriesTests(TestCase):
    def setUp(self):
        self.categories1 = {
            'name': 'food1',
            'description' : 'tastes good!'

        }
        self.categories2 = {
            'name': 'food2',
            'description' : 'tastes good!2'
        }

        self.client = APIClient()
        self.categories1 = Categories.objects.create(**self.categories1)
        self.categories2 = Categories.objects.create(**self.categories2)
        self.url = reverse('categories-list')

    def test_get_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_categories(self):
        new_categories = {
            "categories": [
                {
                    'name': 'food1',
                    'description' : 'tastes good1!'
                },
                {
                    'name': 'food2',
                    'description' : 'tastes good2!'

                }
            ]
        }

        response = self.client.post(self.url, new_categories, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_all_categories(self):
        url = reverse('categories-delete-all')
        self.assertEqual(Categories.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Categories.objects.count(), 0)

    def test_delete_categories_by_id(self):
        url = reverse('categories-delete-by-id', args=[self.categories1.pk])
        self.assertEqual(Categories.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Categories.objects.count(), 1)
        self.assertFalse(Categories.objects.filter(pk=self.categories1.pk).exists())

    def test_get_categories_by_id(self):
        url = reverse('categories-get-by-id', args=[self.categories1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.categories1.name)
        self.assertEqual(response.data['description'], self.categories1.description)



