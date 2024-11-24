from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrderItems
from .serializers import OrderItemsSerializer
from django.http import JsonResponse


@api_view(['POST', 'GET'])
def orderItems_list(request):
    if request.method == 'GET':
        orderItems = OrderItems.objects.all()
        serializer = OrderItemsSerializer(orderItems, many=True)
        return JsonResponse({"orderItems":serializer.data}, safe=False)
    elif request.method == 'POST':
        if not isinstance(request.data.get('orderItems', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of orderItems under the key 'orderItems'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        orderItems_data = request.data.get('orderItems')
        serializer = OrderItemsSerializer(data=orderItems_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def orderItems_delete_by_id(request, pk):
    try:
        orderItems = OrderItems.objects.get(pk=pk)
    except OrderItems.DoesNotExist:
        return Response(
            {"error": "orderItems not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    orderItems.delete()
    return Response(
        {"message": f"orderItems with ID {pk} has been deleted."},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def orderItems_get_by_id(request, pk):
    try:
        orderItems = OrderItems.objects.get(pk=pk)
    except OrderItems.DoesNotExist:
        return Response(
            {"error": "orderItems not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = OrderItemsSerializer(orderItems)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def orderItems_delete_all(request):
    OrderItems.objects.all().delete()
    return Response(
        {"message": "All orderItems have been deleted."},
        status=status.HTTP_200_OK
    )
