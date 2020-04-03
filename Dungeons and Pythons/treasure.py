import random


class Treasure:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)


    def __repr__(self):
        return str(self.__dict__)


    # @staticmethod
    # def get_random_treasure():
    #     return random.choice(treasures)
    #     # self.__dict__ = random.choice(treasures).__dict__


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


# treasures = [
# Weapon(name="The Axe of Destiny", damage=20),
# Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2),
# HealthPotion(name="The potion of Undying", healing=50),
# ManaPotion(name="The potion of Unexhausting", healing=50),

# ]