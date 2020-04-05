class Treasure:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        return str(self.__dict__)


class Spell(Treasure):
    # name, damage, mana_cost, cast_range
    pass


class Weapon(Treasure):
    # name, damage
    pass


class HealthPotion(Treasure):
    # name, healing
    pass


class ManaPotion(Treasure):
    pass
