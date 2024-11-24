from django.http import JsonResponse
from django.shortcuts import render
from .models import Orders
from .serializers import OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == "GET":
        orders = Orders.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse({"orders" : serializer.data}, safe=False)
    
    if request.method == "POST":
        if not isinstance(request.data.get('orders', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of orders under the key 'orders'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        orders_data = request.data.get('orders')
        serializer = OrderSerializer(data=orders_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def order_delete_by_id(request, pk):
    try:
        order = Orders.objects.get(pk=pk)
    except Orders.DoesNotExist:
        return Response(
            {"error": "Order not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    order.delete()
    return Response(
        {"message": f"Order with ID {pk} has been deleted."},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def order_get_by_id(request, pk):
    try:
        order = Orders.objects.get(pk=pk)
    except Orders.DoesNotExist:
        return Response(
            {"error": "Order not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def order_delete_all(request):
    Orders.objects.all().delete()
    return Response(
        {"message": "All orders have been deleted."},
        status=status.HTTP_200_OK
   )