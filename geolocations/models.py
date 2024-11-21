from django.db import models

class Geolocation(models.Model):
    geolocation_zip_code_prefix = models.IntegerField(max_length=200, primary_key=True)
    geolocation_lat = models.FloatField(unique=True)
    geolocation_lng = models.FloatField(unique=True)
    geolocation_city = models.CharField(max_length=200)
    geolocation_state = models.CharField(max_length=200)

    def __str__(self):
        return str(self.geolocation_zip_code_prefix)

