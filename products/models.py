from django.db import models
from categories.models import Categories

class Products(models.Model):
    product_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
    brand = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

