import requests

class WeatherAPI:
    OWM_Endpoint: str
    api_key: str
    weather_params: dict

    def __init__(self, lat, lon, api_key=None):
        self.OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
        self.api_key = "69f04e4613056b159c2761a9d9e664d2"
        self.weather_params = {"lat": lat,
                               "lon": lon,
                               "exclude": "current,minutely,daily",
                               "appid": self.api_key}

    def fetch_weather_data(self):
        try:
            response = requests.get(self.OWM_Endpoint, params=self.weather_params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
