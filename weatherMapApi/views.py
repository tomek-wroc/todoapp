from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .utils import calcBackgroundColor
from .utils import fetchWeather
 
@api_view(['POST'])
# Only authenticated user via Basic auth or session + CSRF token method has an access to this Post endpoind
#@permission_classes([IsAuthenticated])
def getWeatherData(request):
    request_data = request.data
    # Verify if body has location in correct format in POST request
    if 'location' in request_data:
        if not isinstance(request_data['location'], str):
            return Response({'error': 'Location must be a string'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # If 'location' is not provided in the request data, return a bad request response
        return Response({'error': 'Location not provided'}, status=status.HTTP_400_BAD_REQUEST)
   
    location = request_data.get('location')
    response = fetchWeather(location)
    if response.status_code == 200:
        json_response = response.json();        
        # Weather description: clouds, rain, and others. More info under the link: https://openweathermap.org/weather-conditions  
        weather = json_response['weather'][0]['main']
        # Temperature in celsius degress of selected location
        temp = json_response['main']['temp']
        mapped_data = {
            'weather': weather,
            'temp': temp,
            'background_color': calcBackgroundColor(weather, temp)
            }
        return Response(mapped_data, status=status.HTTP_200_OK)
    else:
        return Response("Failed to fetch data from external API", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
