from django.test import TestCase
from orderItems.models import OrderItems
from products.models import Products
from orders.models import Orders
from rest_framework.test import APIClient
from django.urls import reverse
from customers.models import Customer
from rest_framework import status


class TestOrderItems(TestCase):
    def setUp(self):
        self.products1 = Products.objects.create(
            name='Foodx',
            description='Foodx',
            price=23.56,
            stock_quantity=34,
            brand='Haldiram'
        )

        self.products2 = Products.objects.create(
            name='Foodx',
            description='Foodx',
            price=23.56,
            stock_quantity=34,
            brand='Haldiram'
        )

        self.customer1 = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='email@email.com',
            password='password',
            phone_number=1234567890,
            address='123, Main Street, Bangalore'
        )

        self.order1 = Orders.objects.create(
            order_id=1,
            customer_id=self.customer1['customer_id'],
            order_status='Pending',
            total_amount=47.12
        )

        self.orderItem_data_1 = {
            'order_id': self.order1['order_id'],
            'product_id': self.products1['product_id'],
            'quantity': 2,
            'total_price': 47.12,
            'price_per_unit': 23.56
        }

        self.orderItem_data_2 = {
            'order_id': self.order1['order_id'],
            'product_id': self.products1['product_id'],
            'quantity': 2,
            'total_price': 47.12,
            'price_per_unit': 23.56
        }

        self.client = APIClient()
        self.orderItem1 = Products.objects.create(**self.orderItem_data_1)
        self.orderItem2 = Products.objects.create(**self.orderItem_data_2)
        self.url = reverse('products-list')
    
    def test_get_orderItems(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_orderItems(self):
        new_orderItems = [
            {
                'order_id': self.order1['order_id'],
                'product_id': self.products1['product_id'],
                'quantity': 2,
                'total_price': 47.12,
                'price_per_unit': 23.56
            },
            {   
                'order_id': self.order1['order_id'],
                'product_id': self.products1['product_id'],
                'quantity': 2,
                'total_price': 47.12,
                'price_per_unit': 23.56
            }
        ]

        response = self.client.post(self.url, {'orderItems': new_orderItems}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_delete_all_orderItems(self):
        url = reverse('orderItems-delete-all')
        self.assertEqual(OrderItems.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(OrderItems.objects.count(), 0)
        self.assertEqual(response.data['message'], 'All orderItems have been deleted.')

    def test_delete_orderItems_by_id(self):
        url = reverse('orderItems-delete-by-id', args=[self.orderItem1.pk])
        self.assertEqual(Customer.objects.count(), 2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(response.data['message'], f"OrderItems with ID {self.orderItem1.pk} has been deleted.")
        self.assertFalse(Customer.objects.filter(pk=self.orderItem1.pk).exists())

    # def test_get_orderItems_by_id(self):
    #     url = reverse('orderItems-get-by-id', args=[self.orderItem1.pk])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['order_id'], self.orderItem1.order_id)
    #     self.assertEqual(response.data['email'], self.orderItem1.quantity)
    #     self.assertEqual(response.data['phone_number'], self.customer1.phone_number)
    #     self.assertEqual(response.data['address'], self.customer1.address)





        
