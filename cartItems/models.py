from django.db import models
from carts.models import Carts
from products.models import Products

class CartItems(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart_id = models.ForeignKey(Carts, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()