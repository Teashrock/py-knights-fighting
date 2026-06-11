class Potion:
    def __init__(self, json: dict) -> None:
        self.name = json["name"]
        self.power = json["effect"].get("power", 0)
        self.hp = json["effect"].get("hp", 0)
        self.protection = json["effect"].get("protection", 0)
