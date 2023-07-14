import requests

class WeatherAPI:
    yr_endpoint: str
    weather_params: dict

    def __init__(self, lat, lon, api_key=None):
        self.yr_endpoint = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
        self.weather_params = {"lat": lat,
                               "lon": lon}
        self.headers = {
            'User-Agent': 'weatherApp github.com/rekinp/'}

    def fetch_weather_data(self):
        try:
            response = requests.get(self.yr_endpoint, params=self.weather_params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
