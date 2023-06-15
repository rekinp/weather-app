class MessageBuilder:
    def __init__(self, city,
                 condition,
                 hours_to_rain,
                 max_temp,
                 min_temp):
        self.city = city
        self.condition = condition
        self.hours_to_rain = hours_to_rain
        self.max_temp = max_temp
        self.min_temp = min_temp

    @property
    def message(self):
        if self.hours_to_rain > 0:
            return f"{self.city} is going to {self.condition} in {self.hours_to_rain + 1} hours. Temp: {self.min_temp} - {self.max_temp}."
        else:
            return f"{self.city} no rain for next 12 hours. Temp: {self.min_temp} - {self.max_temp}."