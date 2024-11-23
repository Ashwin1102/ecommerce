from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=200)
    description  = models.CharField(max_length=300)

