class Weapon:
    def __init__(self, json: dict) -> None:
        self.name = json["name"]
        self.power = json["power"]
