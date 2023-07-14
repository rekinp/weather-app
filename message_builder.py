class MessageBuilder:
    def __init__(self, city,
                 condition_1h,
                 condition_6h,
                 max_temp,
                 min_temp):
        self.city = city
        self.condition_1h = condition_1h
        self.condition_6h = condition_6h
        self.max_temp = max_temp
        self.min_temp = min_temp

    @property
    def message(self):
        return f"{self.city}:\n" \
               f"Temperature: {self.min_temp} - {self.max_temp}°C.\n" \
               f"Next hour: {self.condition_1h.replace('_', ' ')}\n" \
               f"Next 6 hours: {self.condition_6h.replace('_', ' ')}\n"