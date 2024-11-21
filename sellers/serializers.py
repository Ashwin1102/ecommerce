from rest_framework import serializers
from .models import Sellers

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = '__all__'
        