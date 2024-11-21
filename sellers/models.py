from django.db import models
from geolocations.models import Geolocation

class Sellers(models.Model):
    seller_id = models.CharField(max_length=200, primary_key=True)
    seller_zip_code_prefix = models.ForeignKey(Geolocation, on_delete=models.CASCADE)
    seller_city = models.CharField(max_length=200)
    seller_state = models.CharField(max_length=200)

    def __str__(self):
        return str(self.seller_id)
