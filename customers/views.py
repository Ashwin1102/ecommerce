from django.http import JsonResponse
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse({"customers" : serializer.data}, safe=False)
    
    if request.method == "POST":
        if not isinstance(request.data.get('customers', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of customers under the key 'customers'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        customers_data = request.data.get('customers')
        serializer = CustomerSerializer(data=customers_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)