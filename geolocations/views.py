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
                {"error": "Invalid request body. Expected a list of customers under the key 'customers'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        geolocation_data = request.data.get('geolocations')
        serializer = GeolocationSerializer(data=geolocation_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)