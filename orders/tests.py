from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Orders
from .serializers import OrderSerializer
from customers.models import Customer

class OrdersTestCase(TestCase):
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
            'customer_id': '1326',
            'first_name': 'ash',
            'last_name': "ka",
            "email": "email@email.com",
            "password": "324",
            "phone_number": 123,
            "address": "Beacon St"
        }

        self.order_data_1 = {
            'order_id': '132',
            'customer_id': self.customer_data_1['customer_id'],
            'order_status': "pending",
            "total_amount": 100
        }

        self.order_data_2 = {
            'order_id': '1321',
            'customer_id': self.customer_data_2['customer_id'],
            'order_status': "pending",
            "total_amount": 100
        }

        self.client = APIClient()
        self.customer1 = Customer.objects.create(**self.customer_data_1)
        self.customer2 = Customer.objects.create(**self.customer_data_2)
        self.order_data_1['customer_id'] = self.customer1
        self.order_data_2['customer_id'] = self.customer2
        self.order1 = Orders.objects.create(**self.order_data_1)
        self.order2 = Orders.objects.create(**self.order_data_2)
        self.url = reverse('order-list')

    def test_order_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_order_post(self):
        customer_data_2 = Customer.objects.get(customer_id='1326')
        new_order = {
            'order_id': '1326',
            'customer_id': customer_data_2.customer_id,
            'order_status': "pending",
            "total_amount": 100
        }
        response = self.client.post(self.url, {'orders': [new_order]}, format='json')
        self.assertEqual(response.status_code, 201)


    def test_order_delete_all(self):
        url = reverse('order-delete-all')
        self.assertEqual(Orders.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Orders.objects.count(), 0)
        self.assertEqual(response.data, {"message": "All orders have been deleted."})

    # def test_order_get_by_id(self):
    #     url = reverse('order-get-by-id')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data['order_id'], self.order_data_1['order_id'])
    #     self.assertEqual(response.data['order_status'], self.order_data_1['order_status'])
    #     self.assertEqual(response.data['total_amount'], self.order_data_1['total_amount'])
    #     self.assertEqual(response.data['customer_id'], self.order_data_1['customer_id'])
        
                         