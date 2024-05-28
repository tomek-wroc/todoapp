import requests
from django.conf import settings

'''This function takes a location as input,
constructs a URL to fetch weather data from the OpenWeatherMap API using the location and an API key stored in Django settings,
and returns the response obtained from making a GET request to this URL.'''

def get_seccure_key():
    return settings.OPEN_WEATHER_MAP_API_KEY

def fetchWeather(location):
    weather_map_api_key = get_seccure_key()
    # Apply unit=metric in order to obtain temperature in celsius degrees
    unit = "metric"
    external_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={weather_map_api_key}&units={unit}"
    return requests.get(url=external_api_url)

def fetchWeatherLatLon(latitude, longitude):
    weather_map_api_key = get_seccure_key()
    # Apply unit=metric in order to obtain temperature in celsius degrees
    unit = "metric"
    external_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={weather_map_api_key}&units={unit}"
    return requests.get(url=external_api_url)



'''
This function calculates a background color based on weather conditions and temperature.
It defines three sets of conditions based on temperature ranges and weather descriptions: cold or rainy conditions, warm or cloudy conditions, and hot or sunny conditions.
It then checks the input temperature and weather against these conditions and returns a corresponding background color.
If the input doesn't match any defined conditions, it returns 'white' color by default.
'''


def calcBackgroundColor(weather, temp):
    cold_or_rain_conditions = {'max_temp': 10,
        'weather': "Rain", 'color': 'blue'}
    warm_or_cloudy_conditions = {
        'min_temp': 10, 'max_temp': 25, 'weather': "Clouds", 'color': '#FFA500'}
    hot_or_sunny_conditions = {'min_temp': 25,
        'weather': "Clear", 'color': 'red'}

    # Assumption that 'response' is a dictionary containing temperature and weather information
    if (temp < cold_or_rain_conditions['max_temp']) or weather == cold_or_rain_conditions['weather']:
        return cold_or_rain_conditions['color']
    elif (temp >= warm_or_cloudy_conditions['min_temp'] and temp <= warm_or_cloudy_conditions['max_temp']) or weather == warm_or_cloudy_conditions['weather']:
        return warm_or_cloudy_conditions['color']
    elif (temp > hot_or_sunny_conditions['min_temp']) or (hot_or_sunny_conditions['weather'] == hot_or_sunny_conditions['max']):
        return hot_or_sunny_conditions['color']
    else:
        # If temperature is outside of defined ranges or doesn't match any weather description, set default background color
        return 'white'
