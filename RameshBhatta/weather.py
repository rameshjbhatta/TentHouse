# weather_api/views.py
import requests
from django.http import JsonResponse

def get_weather(request, city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Weather data not available'}, status=500)
