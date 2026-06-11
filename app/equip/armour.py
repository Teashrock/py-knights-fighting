class Armour:
    def __init__(self, json: dict) -> None:
        self.part = json["part"]
        self.protection = json["protection"]

    def __add__(self, other: int) -> int:
        return self.protection + other
