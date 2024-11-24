from django.db import models
from customers.models import Customer

class Carts(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)