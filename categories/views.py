from django.http import JsonResponse
from .models import Categories
from .serializers import CategoriesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == "GET":
        categories = Categories.objects.all()

        serializer = CategoriesSerializer(categories, many=True)
        return JsonResponse({"categories" : serializer.data}, safe=False)

    if request.method == "POST":
        if not isinstance(request.data.get('categories', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of categories under the key 'categories'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        categories_data = request.data.get('categories')
        serializer = CategoriesSerializer(data=categories_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def categories_delete_by_id(request, pk):
    try:
        categories = Categories.objects.get(pk=pk)
    except Categories.DoesNotExist:
        return Response(
            {"error": "Categories not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    categories.delete()
    return Response(
        {"message": f"Categories with ID {pk} has been deleted."},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def categories_get_by_id(request, pk):
    try:
        categories = Categories.objects.get(pk=pk)
    except Categories.DoesNotExist:
        return Response(
            {"error": "Categories not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = CategoriesSerializer(categories)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def categories_delete_all(request):
    Categories.objects.all().delete()
    return Response(
        {"message": "All categories have been deleted."},
        status=status.HTTP_200_OK
    )