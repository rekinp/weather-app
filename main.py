from message_api import MessageAPI
from weather_api import WeatherAPI
from weather_parser import WeatherParser
from message_builder import MessageBuilder
from config import cities
import os

def main():
    messages_to_be_sent = []
    for city in cities:
        weather_data = WeatherAPI(lat=cities[city]["lat"], lon=cities[city]["lon"]).fetch_weather_data()
        weather_parser = WeatherParser(weather_api_response_data=weather_data)
        max_temp = weather_parser.get_max_temperature()
        min_temp = weather_parser.get_min_temperature()
        message_builder = MessageBuilder(city=city,
                                         condition_1h=weather_parser.weather_list[1].next_1_hours,
                                         condition_6h=weather_parser.weather_list[1].next_6_hours,
                                         max_temp=max_temp,
                                         min_temp=min_temp)
        messages_to_be_sent.append(message_builder.message)

    try:
        PUSHOVER_TOKEN = os.environ["PUSHOVER_TOKEN"]
        PUSHOVER_USER = os.environ["PUSHOVER_USER"]
    except KeyError:
        PUSHOVER_TOKEN = "Token not available"
        PUSHOVER_USER = "Token not available"

    ma = MessageAPI(token=PUSHOVER_TOKEN, user=PUSHOVER_USER)
    message_to_be_sent = "\n".join(messages_to_be_sent)
    ma.push_message(message=message_to_be_sent)

if __name__ == "__main__":
    main()