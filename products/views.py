from django.shortcuts import render

from django.http import JsonResponse
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == "GET":
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return JsonResponse({"products" : serializer.data}, safe=False)
    
    if request.method == "POST":
        if not isinstance(request.data.get('products', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of products under the key 'products'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        products_data = request.data.get('products')
        serializer = ProductsSerializer(data=products_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def products_delete_by_id(request, pk):
    try:
        seller = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(
            {"error": "Products not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    seller.delete()
    return Response(
        {"message": f"Products with ID {pk} has been deleted."},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def products_get_by_id(request, pk):
    try:
        seller = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(
            {"error": "Products not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = ProductsSerializer(seller)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def products_delete_all(request):
    Products.objects.all().delete()
    return Response(
        {"message": "All products have been deleted."},
        status=status.HTTP_200_OK
    )