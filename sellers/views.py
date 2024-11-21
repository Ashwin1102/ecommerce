from django.shortcuts import render

from django.http import JsonResponse
from .models import Sellers
from .serializers import SellerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def sellers_list(request):
    if request.method == "GET":
        sellers = Sellers.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return JsonResponse({"sellers" : serializer.data}, safe=False)
    
    if request.method == "POST":
        if not isinstance(request.data.get('sellers', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of sellers under the key 'sellers'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        sellers_data = request.data.get('sellers')
        serializer = SellerSerializer(data=sellers_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
