from __future__ import annotations
try:
    from equip.weapons import Weapon
    from equip.armour import Armour
    from equip.potions import Potion
except ImportError:
    from app.equip.weapons import Weapon
    from app.equip.armour import Armour
    from app.equip.potions import Potion


class Knight:
    def __init__(self, json: dict) -> None:
        self.name = json["name"]
        self.power = json["power"]
        self.hp = json["hp"]
        self.armour = [Armour(armour) for armour in json["armour"]]
        self.weapon = Weapon(json["weapon"])
        self.potion = Potion(json["potion"]) if json["potion"] else None

        self.protection = 0
        for armour in self.armour:
            self.protection += armour.protection

        self.power += self.weapon.power

        if self.potion:
            self.power += self.potion.power
            self.hp += self.potion.hp
            self.protection += self.potion.protection

    def fight(self, other: Knight) -> None:
        other.hp -= (self.power - other.protection)
        self.hp -= (other.power - self.protection)
        if other.hp <= 0:
            other.hp = 0
        if self.hp <= 0:
            self.hp = 0
