from dungeon import Dungeon
import subprocess
from time import sleep
from hero import Hero
from help_library import get_character


def print_intro():
    new_screen()
    intro = 'Hi, a game has just started!\n\n' \
    'You are put in a magic dungeon with TREASURES (T) ' \
    'and your task is to make through the exit (G), but be carefull!\n' \
    'There are ENEMIES (E) that you need to fight and obstacles (#).\n' \
    'To make it easier for you there are checkpoints (C) in the dungeon.\n' \
    'Good luck!\n'
    print(intro)


def print_legend():
    print('LEGEND:')
    print('S - spawning position           ' + 'C - checkpoint')
    print('G - exit of the dungeon         ' + 'T - treasure')
    print('# - obstacle                    ' + 'E - enemy')


def print_dungeon_map(dungeon):
    print('This is your map:')
    print(dungeon.map)


def print_map_with_legend(dungeon):
    print_dungeon_map(dungeon)
    print()
    print_legend()
    print('\n')


def new_screen():
    bashCommand = "clear"
    subprocess.call(bashCommand)


def wait_until_symbol_from_list_of_symbols_is_read_from_console(symbols, message):
    pressed = None
    while True:
        correct_symbol_read = False
        for symbol in symbols:
            if pressed == symbol:
                correct_symbol_read = True
                break
        if correct_symbol_read is True:
            return pressed
            break
        if pressed != None:
            print(str(pressed))
        print(message)
        pressed = str(get_character())[2]
        pressed = pressed.lower()


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
    print()


def print_navigation_legend():
    print('NAVIGATION: w --> up\n'
          '            s --> down\n'
          '            a --> left\n'
          '            d --> right')
    print('\n')


def convert_symbol_pressed_to_direction(symbol_pressed):
    if symbol_pressed == 'w':
        return 'up'
    elif symbol_pressed == 's':
        return 'down'
    elif symbol_pressed == 'a':
        return 'left'
    else:
        return 'right'


def validate_move_from_console(dungeon):
    list_of_symbols = ['w', 's', 'a', 'd']
    message = 'Press w,s,a or d to move ...'
    correct = False
    while correct is False:
        symbol_pressed = wait_until_symbol_from_list_of_symbols_is_read_from_console(list_of_symbols, message)
        direction = convert_symbol_pressed_to_direction(symbol_pressed)
        if dungeon.move_hero(direction):
            print('You moved your hero ', direction)
            correct = True
        else:
            print('You cannot go {dir}, try different move\n'.format(dir=direction))


def show_new_move_screen(dungeon, hero):
    new_screen()
    print_hero_current_state(hero)
    print_navigation_legend()
    print_map_with_legend(dungeon)
    validate_move_from_console(dungeon)

def moving_process(dungeon, hero):
    while True:
        show_new_move_screen(dungeon, hero)


def main():
    print_intro()
    dungeon = Dungeon('level1.txt')
    print_map_with_legend(dungeon)
    symbol = 's'
    message = 'Press s for start'
    wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)
    new_screen()
    hero = create_hero()
    symbol = 'c'
    message = 'Press c for continue ...'
    wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)
    # sleep(1)
    dungeon.spawn(hero)
    moving_process(dungeon, hero)
    
    # while True:
    #     pass


if __name__ == '__main__':
    main()
