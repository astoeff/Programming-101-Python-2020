import random
from playable import Playable
from treasure import Spell, Weapon

def choose_random_spell_from_file():
        try:
            with open('spells.txt', 'r') as f:
                spells_in_file = f.read().splitlines()
                spell_args_string = random.choice(spells_in_file)
                if spell_args_string == 'None':                   
                    return None
                args = spell_args_string.split(',')
                spell = Spell(name=args[0], damage=int(args[1]), mana_cost=int(args[2]), cast_range=int(args[3]))               
                return spell
        except Exception as e:
           print(e)

def choose_random_weapon_from_file():
        try:
            with open('weapons.txt', 'r') as f:
                weapons_in_file = f.read().splitlines()
                weapon_args_string = random.choice(weapons_in_file)
                if weapon_args_string == 'None':                   
                    return None
                args = weapon_args_string.split(',')
                weapon = Weapon(name=args[0], damage=int(args[1]))               
                return weapon
        except Exception as e:
           print(e)

class Enemy(Playable):
    def __init__(self):
        self.health = random.randint(50,100)
        self.mana = random.randint(50,100)
        self.damage = random.randint(10,50)
        self.weapon = choose_random_weapon_from_file()
        self.spell = choose_random_spell_from_file()

    def attack(self, **kwargs):
        result_from_attack = 0
        try:
            result_from_attack = super().attack(**kwargs)
        except Exception as e:
            raise e
        if result_from_attack != None:
            return result_from_attack
        return self.damage
        