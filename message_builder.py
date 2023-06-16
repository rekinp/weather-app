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
        msg_header = f"{self.city}:\n" \
                   f"Temperature: {self.min_temp} - {self.max_temp}°C."
        if self.hours_to_rain > 0:
            return msg_header + f"\nIt is going to {self.condition} in {self.hours_to_rain + 1} hours. "
        else:
            return msg_header + f"\n No rain for the next 12 hours."