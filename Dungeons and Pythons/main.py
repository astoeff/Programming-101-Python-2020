from dungeon import Dungeon
import subprocess
from time import sleep
from hero import Hero
from help_library import get_character


def print_intro():
    intro = 'Hi, a game has just started!\n\n' \
    'You are put in a magic dungeon with TREASURES (T) ' \
    'and your task is to make through the exit (G), but be carefull!\n' \
    'There are ENEMIES (E) that you need to fight and obstacles (#).\n' \
    'To make it easier for you there are checkpoints (C) in the dungeon.\n' \
    'Good luck!\n'
    print(intro)


def print_legend():
    print('LEGEND:')
    print('S - spawning position')
    print('C - checkpoint')
    print('G - exit of the dungeon')
    print('T - treasure')
    print('# - obstacle')
    print('E - enemy')


def print_dungeon_map(dungeon):
    print('This is your map:')
    print(dungeon.map)


def print_map_with_legend(dungeon):
    print_dungeon_map(dungeon)
    print()
    print_legend()


def new_screen():
    bashCommand = "clear"
    subprocess.call(bashCommand)


def wait_until_symbol_is_read_from_console(symbol, message):
    pressed = None
    while str(pressed).lower() != symbol:
        print(message)
        pressed = str(get_character())[2]
        print(str(pressed))


def create_hero():
    print('Now enter name and title for your hero:')
    print('Example: Bron, Dragonslayer\n')
    name = input('Name: ')
    title = input('Title: ')
    new_screen()
    h = Hero(name=name, title=title, health=100, mana=100, mana_regeneration_rate=2)
    print('Information for hero:\n')
    h.print_hero()
    return h


def print_hero_current_state(hero):
    upper_border = ''
    info = []
    info.append(hero.known_as())
    info.append('HEALTH = ' + str(hero.health))
    info.append('MANA = ' + str(hero.mana))
    info.append('WEAPON = ' + str(hero.weapon))
    info.append('SPELL = ' + str(hero.spell))
    max_len = max([len(i) for i in info])
    for i in range(max_len + 2):
        upper_border += '*'
    print(upper_border)

    for i in range(5):
        spaces_count = max_len - 1 - len(info[i])
        if len(info[i]) != max_len:
            spaces = ' '
        else:
            spaces = ''
        for j in range(spaces_count):
            spaces += ' '
        print('*' + info[i] + spaces + '*')
    print(upper_border)
    print('\n')


def main():
    print_intro()
    dungeon = Dungeon('level1.txt')
    print_map_with_legend(dungeon)
    symbol = 's'
    message = 'Press s for start'
    wait_until_symbol_is_read_from_console(symbol, message)
    new_screen()
    hero = create_hero()
    sleep(1)
    new_screen()
    dungeon.spawn(Hero)
    print_hero_current_state(hero)
    print_map_with_legend(dungeon)
    sleep(10)
    # while True:
    #     pass


if __name__ == '__main__':
    main()
