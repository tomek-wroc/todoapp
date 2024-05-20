import requests
from django.conf import settings
 
'''This function takes a location as input,
constructs a URL to fetch weather data from the OpenWeatherMap API using the location and an API key stored in Django settings,
and returns the response obtained from making a GET request to this URL.'''
def fetchWeather(location):
    weather_map_api_key = settings.OPEN_WEATHER_MAP_API_KEY
    # Apply unit=metric in order to obtain temperature in celsius degrees
    unit = "metric"
    key_len = settings.API_KEY_LEN
    if key_len == 32:
        external_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={weather_map_api_key}&units={unit}"
    else: 
        external_api_url = f"http://api.weatherapi.com/v1/current.json?key={weather_map_api_key}&q={location}&aqi=no"
    return requests.get(url=external_api_url)
 
'''
This function calculates a background color based on weather conditions and temperature.
It defines three sets of conditions based on temperature ranges and weather descriptions: cold or rainy conditions, warm or cloudy conditions, and hot or sunny conditions.
It then checks the input temperature and weather against these conditions and returns a corresponding background color.
If the input doesn't match any defined conditions, it returns 'white' color by default.
'''
def calcBackgroundColor(weather, temp):
    cold_or_rain_conditions = {'max_temp': 10,'weather': "Rain", 'color': 'blue'}
    warm_or_cloudy_conditions = {'min_temp': 10, 'max_temp': 25, 'weather': "Clouds", 'color': '#FFA500'}
    hot_or_sunny_conditions = {'min_temp': 25, 'weather': "Clear", 'color': 'red'}
    key_len = settings.API_KEY_LEN
 
    # Assumption that 'response' is a dictionary containing temperature and weather information
    if key_len == 32:
        if (temp < cold_or_rain_conditions['max_temp']) or weather == cold_or_rain_conditions['weather']:
            return cold_or_rain_conditions['color']
        elif (temp >= warm_or_cloudy_conditions['min_temp'] and temp <= warm_or_cloudy_conditions['max_temp']) or weather == warm_or_cloudy_conditions['weather']:
            return warm_or_cloudy_conditions['color']
        elif (temp > hot_or_sunny_conditions['min_temp']) or (hot_or_sunny_conditions['weather'] == hot_or_sunny_conditions['max']):
            return hot_or_sunny_conditions['color']
        else:
            # If temperature is outside of defined ranges or doesn't match any weather description, set default background color
            return 'white'
    else:
        if (temp < cold_or_rain_conditions['max_temp']) or weather == cold_or_rain_conditions['weather']:
            return cold_or_rain_conditions['color']
        elif (temp >= warm_or_cloudy_conditions['min_temp'] and temp <= warm_or_cloudy_conditions['max_temp']) or weather == warm_or_cloudy_conditions['weather']:
            return warm_or_cloudy_conditions['color']
        elif (temp > hot_or_sunny_conditions['min_temp']) or (hot_or_sunny_conditions['weather'] == hot_or_sunny_conditions['max']):
            return hot_or_sunny_conditions['color']
        else:
            # If temperature is outside of defined ranges or doesn't match any weather description, set default background color
            return 'white'
 