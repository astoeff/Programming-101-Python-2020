from utils import *
import time


def create_pond(pond_size, rose_frogs, blue_frogs, free_lily):
    pond = ''
    for pos in range(pond_size):
        if pos == free_lily:
            pond += '_'
        elif pos in rose_frogs:
            pond += '@'
        else:
            pond += '#'
    return pond


def find_position_of_movable_rose_frog(rose_frogs, free_lily):
    return find_biggest_number_in_sorted_list_less_than_given_number_and_swap_them(rose_frogs, free_lily)


def find_position_of_movable_blue_frog(blue_frogs, free_lily):
    return find_least_number_in_sorted_list_bigger_than_given_number_and_swap_them(blue_frogs, free_lily)


def is_color_moveable(position):
    return True if position != -1 else False


def swap_frog_position_and_lily_position_in_frogs_list(frogs, frog_position, free_lily):
    swapper = frogs[frog_position]
    frogs[frog_position] = free_lily
    free_lily = swapper
    return (frogs, free_lily)


def swap_frog_position_and_lily_position_in_pond_string(pond, frog_position, free_lily, frog_symbol):
    pond_as_array = list(pond)
    pond_as_array[frog_position] = frog_symbol
    pond_as_array[free_lily] = '_'
    return ''.join(pond_as_array)



def play(pond_size):
    if pond_size % 2 == 0:
        raise ValueError(f'Invalid pond_size:{pond_size} given ')
    else:
        rose_frogs = [i for i in range(0, pond_size // 2)]
        blue_frogs = [i for i in range(pond_size // 2 + 1, pond_size)]
        free_lily = pond_size // 2
        rose_frog_final_position = pond_size - 1
        blue_frog_final_position = 0
        pond = create_pond(pond_size, rose_frogs, blue_frogs, free_lily)
        result = pond[::-1]
        pos = 1
        print(f'Start:   {pond}')
        while True:
            position_in_list_of_rose_movable_frog = find_position_of_movable_rose_frog(rose_frogs, free_lily)
            position_in_list_of_blue_movable_frog = find_position_of_movable_blue_frog(blue_frogs, free_lily)
            already_moved = False
            if is_color_moveable(position_in_list_of_rose_movable_frog):
                condition = True
                if position_in_list_of_rose_movable_frog != 0:
                    last_before_movable = rose_frogs[position_in_list_of_rose_movable_frog - 1]
                    condition = free_lily - last_before_movable == 2
                if free_lily - 1 in blue_frogs and free_lily + 1 in blue_frogs:
                    condition = True
                if free_lily + 1 in blue_frogs and condition:
                    swapper = rose_frogs[position_in_list_of_rose_movable_frog]
                    rose_frogs[position_in_list_of_rose_movable_frog] = free_lily
                    free_lily = swapper
                    pond_as_array = list(pond)
                    pond_as_array[rose_frogs[position_in_list_of_rose_movable_frog]] = '@'
                    pond_as_array[free_lily] = '_'
                    pond = ''.join(pond_as_array)
                    already_moved = True
                elif free_lily == rose_frog_final_position:
                    swapper = rose_frogs[position_in_list_of_rose_movable_frog]
                    rose_frogs[position_in_list_of_rose_movable_frog] = free_lily
                    free_lily = swapper
                    pond_as_array = list(pond)
                    pond_as_array[rose_frogs[position_in_list_of_rose_movable_frog]] = '@'
                    pond_as_array[free_lily] = '_'
                    pond = ''.join(pond_as_array)
                    rose_frog_final_position -= 1
                    already_moved = True
            if not already_moved:
                if is_color_moveable(position_in_list_of_blue_movable_frog):
                    if free_lily - 1 in rose_frogs:
                        swapper = blue_frogs[position_in_list_of_blue_movable_frog]
                        blue_frogs[position_in_list_of_blue_movable_frog] = free_lily
                        free_lily = swapper
                        pond_as_array = list(pond)
                        pond_as_array[blue_frogs[position_in_list_of_blue_movable_frog]] = '#'
                        pond_as_array[free_lily] = '_'
                        pond = ''.join(pond_as_array)
                    elif free_lily == blue_frog_final_position:
                        swapper = blue_frogs[position_in_list_of_blue_movable_frog]
                        blue_frogs[position_in_list_of_blue_movable_frog] = free_lily
                        free_lily = swapper
                        pond_as_array = list(pond)
                        pond_as_array[blue_frogs[position_in_list_of_blue_movable_frog]] = '#'
                        pond_as_array[free_lily] = '_'
                        pond = ''.join(pond_as_array)
                        blue_frog_final_position += 1
            if pond == result:
                print(f'Result: {pond}')
                break
            print(f'Step {pos}: {pond}')
            # time.sleep(3)          
            pos += 1
        print(f'\nSolved in {pos} steps')


play(101)
