from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItems
from .serializers import CartItemsSerializer
from django.http import JsonResponse


@api_view(['POST', 'GET'])
def cartItems_list(request):
    if request.method == 'GET':
        cartItems = CartItems.objects.all()
        serializer = CartItemsSerializer(cartItems, many=True)
        return JsonResponse({"cartItems":serializer.data}, safe=False)
    elif request.method == 'POST':
        if not isinstance(request.data.get('cartItems', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of cartItems under the key 'cartItems'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        cartItems_data = request.data.get('cartItems')
        serializer = CartItemsSerializer(data=cartItems_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def cartItems_delete_by_id(request, pk):
    try:
        cartItems = CartItems.objects.get(pk=pk)
    except CartItems.DoesNotExist:
        return Response(
            {"error": "cartItems not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    cartItems.delete()
    return Response(
        {"message": f"cartItems with ID {pk} has been deleted."},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def cartItems_get_by_id(request, pk):
    try:
        cartItems = CartItems.objects.get(pk=pk)
    except CartItems.DoesNotExist:
        return Response(
            {"error": "cartItems not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = CartItemsSerializer(cartItems)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def cartItems_delete_all(request):
    CartItems.objects.all().delete()
    return Response(
        {"message": "All cartItems have been deleted."},
        status=status.HTTP_200_OK
    )

