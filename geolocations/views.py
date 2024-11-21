from django.http import JsonResponse
from .models import Geolocation
from .serializers import GeolocationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def geolocation_list(request):
    if request.method == "GET":
        geolocations = Geolocation.objects.all()

        print("geolocations ", geolocations)
        serializer = GeolocationSerializer(geolocations, many=True)
        return JsonResponse({"geolocations" : serializer.data}, safe=False)

    if request.method == "POST":
        if not isinstance(request.data.get('geolocations', None), list):
            return Response(
                {"error": "Invalid request body. Expected a list of geolocation under the key 'geolocations'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        geolocation_data = request.data.get('geolocations')
        serializer = GeolocationSerializer(data=geolocation_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def geolocation_delete_by_id(request, pk):
    try:
        geolocation = Geolocation.objects.get(pk=pk)
    except Geolocation.DoesNotExist:
        return Response(
            {"error": "Geolocation not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    geolocation.delete()
    return Response(
        {"message": f"Geolocation with ID {pk} has been deleted."},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def geolocation_get_by_id(request, pk):
    try:
        geolocation = Geolocation.objects.get(pk=pk)
    except Geolocation.DoesNotExist:
        return Response(
            {"error": "Geolocation not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = GeolocationSerializer(geolocation)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def geolocation_delete_all(request):
    Geolocation.objects.all().delete()
    return Response(
        {"message": "All geolocation have been deleted."},
        status=status.HTTP_200_OK
    )