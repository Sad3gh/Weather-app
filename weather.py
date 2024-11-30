import requests


class Weather:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_weather(self, city):
        """ Fetch current weather for a city """
        params = {
            'q': city,
            'app_id': self.api_key,
            'units': 'metric'  # Change to 'imperial' for Fahrenheit
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_forecast(self, city):
        """Fetch weather forecast for a city."""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.FORECAST_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
