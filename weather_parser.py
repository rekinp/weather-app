from model_weather import Weather
from typing import List
from datetime import datetime

class WeatherParser:
    def __init__(self, weather_api_response_data):
        self.weather_list = self.parse_weather_data(weather_api_response_data)

    @staticmethod
    def parse_weather_data(weather_api_response_data):
        weather_timeseries = weather_api_response_data["properties"]["timeseries"]
        now = datetime.now().strftime('%Y-%m-%dT%H:00:00Z')
        times = [t["time"] for t in weather_timeseries]
        weather_slice = weather_timeseries[:12] if now not in times else \
        weather_timeseries[times.index(now):times.index(now) + 12]
        weather_list: List[Weather] = []

        for hour in weather_slice:
            weather = Weather(id=str(hour['time']),
                              temperature=hour['data']['instant']['details']['air_temperature'],
                              wind=hour['data']['instant']['details']['wind_speed'],
                              next_1_hours=hour['data']['next_1_hours']['summary']['symbol_code'],
                              next_6_hours=hour['data']['next_6_hours']['summary']['symbol_code'],
                              next_12_hours=hour['data']['next_12_hours']['summary']['symbol_code'])
            weather_list.append(weather)
        return weather_list

    def get_max_temperature(self):
        temperatures = [w.temperature for w in self.weather_list]
        return max(temperatures)

    def get_min_temperature(self):
        temperatures = [w.temperature for w in self.weather_list]
        return min(temperatures)
