from dungeon import Dungeon
import subprocess
from time import sleep
from hero import Hero
from help_library import get_character
from treasure import Treasure


def print_intro():
    new_screen()
    intro = 'Hi, a game has just started!\n\n' \
    'You are put in a magic dungeon with TREASURES (T) ' \
    'and your task is to make through the exit (G), but be carefull!\n' \
    'There are ENEMIES (E) that you need to fight and obstacles (#).\n' \
    'You can attack your enemies from a distance by spell but only if the range of the spell allows it.\n'\
    'To make it easier for you, there are checkpoints (C) in the dungeon.\n' \
    'Your hero respawns on the latest checkpoint.\n'\
    'If you are dead and have not go through any checkpoints this life, you lose the game!\n'\
    'Good luck!\n'
    print(intro)

def print_dungeon_map(dungeon):
    print('This is your map:')
    print(dungeon.map)

def print_legend():
    print('LEGEND:')
    print('S - spawning position           ' + 'C - checkpoint')
    print('G - exit of the dungeon         ' + 'T - treasure')
    print('# - obstacle                    ' + 'E - enemy')

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


def execute_intro():
    print_intro()
    symbol = 'c'
    message = 'Press c for continue ...'
    wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)
    new_screen()


def wait_for_continue_command():
    symbol = 'c'
    message = 'Press c for continue ...'
    wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)


def start_game():
    symbol = 's'
    message = 'Press s to start a the game ...'
    wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)
    new_screen()


def create_hero():
    print('Now enter name and title for your hero:')
    print('Example: Bron, Dragonslayer\n')
    name = input('Name: ')
    title = input('Title: ')
    new_screen()
    h = Hero(name=name, title=title, health=100, mana=100, mana_regeneration_rate=2)
    print('Information for hero:\n')
    h.print_hero()
    wait_for_continue_command()
    return h


def print_hero_current_state(hero):
    upper_border = ''
    info = []
    info.append(hero.known_as())
    info.append('HEALTH = ' + str(hero.health))
    info.append('MANA = ' + str(hero.mana))
    if str(hero.weapon)[9:] == '':
        info.append('WEAPON = ' + 'None')
    else:
        info.append('WEAPON = ' + str(hero.weapon)[9:])
    if str(hero.spell)[7:] == '':
        info.append('SPELL = ' + 'None')
    else:
        info.append('SPELL = ' + str(hero.spell)[7:])
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
          '            d --> right\n'
          '            x --> attack')
    print('\n')


def wait_for_move():
    symbols = ['w', 's', 'a', 'd', 'x']
    message = 'Press w,s,a, d to move or x to attack from distance by spell ...\n'
    pressed = wait_until_symbol_from_list_of_symbols_is_read_from_console(symbols, message)
    return pressed


def read_direction_from_console():
    list_of_symbols = ['w', 's', 'a', 'd']
    message = 'Press w,s,a or d to select direction'
    symbol_pressed = wait_until_symbol_from_list_of_symbols_is_read_from_console(list_of_symbols, message)
    return convert_symbol_pressed_to_direction(symbol_pressed)


def convert_symbol_pressed_to_direction(symbol_pressed):
    if symbol_pressed == 'w':
        return 'up'
    elif symbol_pressed == 's':
        return 'down'
    elif symbol_pressed == 'a':
        return 'left'
    elif symbol_pressed == 'd':
        return 'right'


def show_attack_from_distance_when_having_spell(dungeon, direction):
    print('Hero attack ', direction)
    dungeon.hero_attack()
    wait_for_continue_command()

def show_attack_screen(dungeon):
    new_screen()
    print_dungeon_map(dungeon)
    print()
    direction = read_direction_from_console()
    if dungeon.hero.spell is None:
        new_screen()
        print('You do not have any spells to attack.\n'\
              'Move to find treasures which might give you spells!\n')
        wait_for_continue_command()
    else:
        show_attack_from_distance_when_having_spell(dungeon, direction)


def show_treasure_screen(treasure):
    new_screen()
    print('You just received:')
    print(treasure)
    print()
    wait_for_continue_command()


def select_screen_depending_on_pressed_key(dungeon, hero, pressed):
    if pressed == 'x':
        show_attack_screen(dungeon)
    else:
        direction = convert_symbol_pressed_to_direction(pressed)
        move_result = dungeon.move_hero(direction)
        if move_result == 'E':
            #fight_enemy_screen
            pass
        elif move_result == 'C':
            #checkpoint_screen
            pass
        elif move_result is True:
            pass
        elif move_result is False:
            pass
        else:
            show_treasure_screen(move_result)
        


def show_move_screen(dungeon, hero):
    new_screen()
    print_hero_current_state(hero)
    print_navigation_legend()
    print_map_with_legend(dungeon)
    move = wait_for_move()
    select_screen_depending_on_pressed_key(dungeon, hero, move)



def play(dungeon, hero):
    dungeon.spawn(hero)
    while True:
        show_move_screen(dungeon, hero)  


def main():
    execute_intro()
    dungeon = Dungeon('level1.txt')
    print_map_with_legend(dungeon)
    start_game()
    hero = create_hero()
    play(dungeon, hero)
    # print_map_with_legend(dungeon)
    # symbol = 's'
    # message = 'Press s for start'
    # wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)
    # new_screen()
    
    # symbol = 'c'
    # message = 'Press c for continue ...'
    # wait_until_symbol_from_list_of_symbols_is_read_from_console([symbol], message)
    # dungeon.spawn(hero)
    # moving_process(dungeon, hero)
    
    # while True:
    #     pass


if __name__ == '__main__':
    main()