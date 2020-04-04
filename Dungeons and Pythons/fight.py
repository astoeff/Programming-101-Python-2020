from constants import (PLAYER_ATTACK_BY_SPELL_STRING,
                       PLAYER_ATTACK_BY_WEAPON_STRING)
from playable import Playable


def flip_direction(direction):
        if direction:
            if direction == 'up':
                return 'down'
            elif direction == 'down':
                return 'up'
            elif direction == 'left':
                return 'right'
            elif direction == 'right':
                return 'left'
            else:
                raise ValueError
        else:
            return direction


class Fight:
    def __init__(self, hero, enemy, distance=0, direction=0):
        assert isinstance(hero, Playable)
        assert isinstance(enemy, Playable)


        self.hero = hero
        self.enemy = enemy
        self.distance = distance
        self.direction = flip_direction(direction)

        self.hero.enough_mana = True
        self.enemy.enough_mana = False

        self.happened = (f'''
A fight is started between our {self.hero} and {self.enemy}''')

        while self.hero.is_alive() and self.enemy.is_alive():
            self.hero_on_turn()
            self.enemy_on_turn()
            break

        if self.hero.is_alive():
            self.happened += (f'''
Enemy is dead''')
        else:
            self.happened += (f'''
Hero is dead''')

    def __repr__(self):
        return self.happened

    def set_attack(self):
        if not self.distance:
            if self.hero.spell:
                if self.hero.weapon:
                    if self.hero.can_cast():
                        if self.hero.spell.damage >= self.hero.weapon.damage:
                            self.attack = PLAYER_ATTACK_BY_SPELL_STRING
                        else:
                            self.attack = PLAYER_ATTACK_BY_WEAPON_STRING
                    else:
                        self.attack = PLAYER_ATTACK_BY_WEAPON_STRING
                        if self.hero.enough_mana:
                            self.hero.enough_mana = False
                            self.happened += (f'''
Hero does not have mana for another {self.hero.spell}.''')
                else:
                    self.attack = PLAYER_ATTACK_BY_SPELL_STRING
            else:
                self.attack = PLAYER_ATTACK_BY_WEAPON_STRING
        else:
            self.attack = PLAYER_ATTACK_BY_SPELL_STRING

        if self.attack == PLAYER_ATTACK_BY_WEAPON_STRING:
            self.happened += (f'''
Hero hits with {self.hero.weapon})''')
        else:
            self.happened += (f'''
Hero casts a {self.hero.spell.name}, hits enemy''')

    def hero_on_turn(self):
        self.set_attack()

        damage = self.hero.attack(by=self.attack)
        self.enemy.take_damage(damage)
        self.happened += f''' for {damage} dmg.\
         Enemy health is {self.enemy.health}'''

    def enemy_on_turn(self):
        if self.distance:
            if self.enemy.can_cast():
                self.enemy.enough_mana = True
                attack = PLAYER_ATTACK_BY_SPELL_STRING
            else:
                if self.enemy.enough_mana:
                    self.enemy.enough_mana = False
                    self.happened += (f'''
Enemy does not have mana for another {self.hero.spell}.''')
                self.distance -= 1
                self.happened += (f'''
Enemy moves one square to the {self.direction} in order to get to the hero.\
 This is his move.''')
        else:
            pass
