from constants import (PLAYER_ATTACK_BY_SPELL_STRING,
                       PLAYER_ATTACK_BY_WEAPON_STRING)
from enemy import Enemy
from hero import Hero
from playable import Playable
from treasure import Spell, Weapon


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
        self.direction = direction
        self.opposite_direction = flip_direction(direction)

        self.hero.enough_mana = True
        self.enemy.enough_mana = False

        self.happened = (f'''
A fight is started between our {self.hero} and {self.enemy}''')

        while True:
            self.hero_on_turn()
            if not self.enemy.is_alive():
                self.happened += (f'''
Enemy is dead
''')
                break

            self.enemy_on_turn()
            if not self.hero.is_alive():
                self.happened += (f'''
Hero is dead
''')
                break

    def __repr__(self):
        return self.happened

    def set_attack(self, playable):
        if not self.distance:
            if playable.spell:
                if playable.weapon:
                    if playable.can_cast():
                        if playable.spell.damage >= playable.weapon.damage:
                            playable.attacking = PLAYER_ATTACK_BY_SPELL_STRING
                        else:
                            playable.attacking = PLAYER_ATTACK_BY_WEAPON_STRING
                    else:
                        playable.attacking = PLAYER_ATTACK_BY_WEAPON_STRING
                        if playable.enough_mana:
                            playable.enough_mana = False
                            self.happened += (f'''
Hero does not have mana for another {self.hero.spell.name}.''')
                elif playable.can_cast():
                    playable.attacking = PLAYER_ATTACK_BY_SPELL_STRING
                else:
                    playable.attacking = 0
                    if isinstance(playable, Hero):
                        self.happened += f'''
Hero has nothing to do.'''
                    elif isinstance(playable, Enemy):
                        self.enemy.attacking = 0
                        self.happened += (f'''
Enemy hits hero''')
            else:
                playable.attacking = PLAYER_ATTACK_BY_WEAPON_STRING
        elif playable.can_cast():
            playable.attacking = PLAYER_ATTACK_BY_SPELL_STRING
        else:
            self.move(playable)
            playable.attacking = None

        if playable.attacking:
            if playable.attacking == PLAYER_ATTACK_BY_WEAPON_STRING:
                if isinstance(playable, Hero):
                    self.happened += (f'''
Hero hits with {self.hero.weapon.name}''')
                elif isinstance(playable, Enemy):
                    if self.enemy.weapon:
                        self.happened += (f'''
Enemy hits with {self.enemy.weapon.name}''')
                    else:
                        self.enemy.attacking = 0
                        self.happened += (f'''
Enemy hits hero''')
                else:
                    raise ValueError
            elif playable.attacking == PLAYER_ATTACK_BY_SPELL_STRING:
                if isinstance(playable, Hero):
                    self.happened += (f'''
Hero casts a {self.hero.spell.name}, hits enemy''')
                elif isinstance(playable, Enemy):
                    self.happened += (f'''
Enemy casts a {self.enemy.spell.name}, hits hero''')
                else:
                    raise ValueError
            else:
                raise ValueError

    def hero_on_turn(self):
        self.set_attack(self.hero)
        if self.hero.attacking:
            damage = self.hero.attack(by=self.hero.attacking)
            self.enemy.take_damage(damage)
            self.happened += f''' for {damage} dmg.\
 Enemy health is {self.enemy.health}'''

    def enemy_on_turn(self):
        self.set_attack(self.enemy)
        if self.enemy.attacking:
            damage = self.enemy.attack(by=self.enemy.attacking)
        else:
            damage = self.enemy.attack()
        self.hero.take_damage(damage)
        self.happened += f''' for {damage} dmg.\
 Hero health is {self.hero.health}'''

    def move(self, playable):
        self.distance -= 1
        if isinstance(playable, Enemy):
            self.happened += (f'''
Enemy moves one square to the {self.opposite_direction} in\
 order to get to the hero. This is his move.''')
        elif isinstance(playable, Hero):
            self.happened += (f'''
Hero moves one square to the {self.direction} in\
 order to get to the enemy. This is his move.''')
        else:
            raise ValueError


if __name__ == '__main__':
    h = Hero(name="Bron", title="Dragonslayer",
             health=100, mana=100, mana_regeneration_rate=2)
    # h.learn(Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2))
    h.equip(Weapon(name="The Axe of Destiny", damage=20))
    e = Enemy()

    print(Fight(h, e))
