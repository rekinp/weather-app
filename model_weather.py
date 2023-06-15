class Weather:
    id: int
    main: str
    description: str
    icon: str
    temperature: float

    def __init__(self, id: int,
                 main: str,
                 description: str,
                 icon: str,
                 temperature: float):
        self.id = id
        self.main = main
        self.description = description
        self.icon = icon
        self.temperature = temperature
