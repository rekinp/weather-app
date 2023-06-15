from model_weather import Weather
from typing import List

class WeatherParser:
    def __init__(self, weather_api_response_data):
        self.weather_list = self.parse_weather_data(weather_api_response_data)

    @staticmethod
    def parse_weather_data(weather_api_response_data):
        weather_slice = weather_api_response_data['hourly'][:12]
        weather_list: List[Weather] = []

        for hour in weather_slice:
            weather = Weather(int(hour['weather'][0]['id']),
                              hour['weather'][0]['main'],
                              hour['weather'][0]['description'],
                              hour['weather'][0]['icon'],
                              hour["temp"])
            weather_list.append(weather)
        return weather_list

    def when_is_going_to_rain(self):
        for i, weather in  enumerate(self.weather_list):
            if weather.id < 700:
                return i
        return 0

    def get_max_temperature(self):
        temperatures = [w.temperature for w in self.weather_list]
        return round(self.kelvin_to_celcius(max(temperatures)), 1)

    def get_min_temperature(self):
        temperatures = [w.temperature for w in self.weather_list]
        return round(self.kelvin_to_celcius(min(temperatures)), 1)

    def kelvin_to_celcius(self, kelvin_degrees):
        c = 273.15
        return kelvin_degrees - c