from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_id
