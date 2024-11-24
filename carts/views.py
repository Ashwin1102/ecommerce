from django.http import JsonResponse
from django.shortcuts import render
from .models import Carts
from .serializers import CartsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def carts_list(request):
    if request.method == "GET":
        carts = Carts.objects.all()
        serializer = CartsSerializer(carts, many=True)
        return JsonResponse({"carts" : serializer.data}, safe=False)
    
    if request.method == "POST":
        if not isinstance(request.data.get('carts', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of carts under the key 'carts'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        carts_data = request.data.get('carts')
        serializer = CartsSerializer(data=carts_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def carts_delete_by_id(request, pk):
    try:
        carts = Carts.objects.get(pk=pk)
    except Carts.DoesNotExist:
        return Response(
            {"error": "carts not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    carts.delete()
    return Response(
        {"message": f"carts with ID {pk} has been deleted."},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def carts_get_by_id(request, pk):
    try:
        carts = Carts.objects.get(pk=pk)
    except Carts.DoesNotExist:
        return Response(
            {"error": "carts not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = CartsSerializer(carts)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def carts_delete_all(request):
    Carts.objects.all().delete()
    return Response(
        {"message": "All carts have been deleted."},
        status=status.HTTP_200_OK
   )