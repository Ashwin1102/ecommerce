from django.db import models
from geolocations.models import Geolocation

class Customer(models.Model):
    customer_id = models.CharField(max_length=200, primary_key=True)
    customer_unique_id = models.CharField(max_length=200, unique=True)
    customer_zip_code_prefix = models.ForeignKey(Geolocation, on_delete=models.CASCADE)
    customer_city = models.CharField(max_length=200)
    customer_state = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_id
