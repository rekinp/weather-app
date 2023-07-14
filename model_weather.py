class Weather:
    id: str
    temperature: float
    next_1_hours: str
    next_6_hours: str
    next_12_hours: str

    def __init__(self, id: str,
                 temperature: float,
                 wind: float,
                 next_1_hours: str,
                 next_6_hours: str,
                 next_12_hours: str):
        self.id = id
        self.temperature = temperature
        self.wind = wind
        self.next_1_hours = next_1_hours
        self.next_6_hours = next_6_hours
        self.next_12_hours = next_12_hours
