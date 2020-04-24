from utils import *
import constants
import time


def create_pond(pond_size, rose_frogs, blue_frogs, free_lily):
    pond = ''
    for pos in range(pond_size):
        if pos == free_lily:
            pond += constants.FREE_LILLY_SYMBOL
        elif pos in rose_frogs:
            pond += constants.ROSE_FROG_SYMMBOL
        else:
            pond += constants.BLUE_FROG_SYMBOL
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


def move_rose_frog()

def play(frogs_per_side):
    assert frogs_per_side >= 0, 'Enter non-negative number of frogs per side'
    pond_size = frogs_per_side * 2 + 1
    rose_frogs = [i for i in range(0, frogs_per_side)]
    blue_frogs = [i for i in range(frogs_per_side + 1, pond_size)]
    free_lily = pond_size // 2
    rose_frog_final_position = pond_size - 1
    blue_frog_final_position = 0
    pond = create_pond(pond_size, rose_frogs, blue_frogs, free_lily)
    result = pond[::-1]
    step_count = 1
    print(f'Start:   {pond}')
    while True:
        position_in_list_of_rose_movable_frog = find_position_of_movable_rose_frog(rose_frogs, free_lily)
        position_in_list_of_blue_movable_frog = find_position_of_movable_blue_frog(blue_frogs, free_lily)
        already_moved = False
        free_lily_left_neighbour = free_lily - 1
        free_lily_right_neighbour = free_lily + 1
        if is_color_moveable(position_in_list_of_rose_movable_frog):
            condition_for_moving = True

            if position_in_list_of_rose_movable_frog != 0:
                last_before_movable = rose_frogs[position_in_list_of_rose_movable_frog - 1]
                condition_for_moving = free_lily - last_before_movable == 2

            if free_lily_left_neighbour in blue_frogs and free_lily_right_neighbour in blue_frogs:  #situation: @#_#
                condition_for_moving = True

            if free_lily_right_neighbour in blue_frogs and condition_for_moving:
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
        print(f'Step {step_count}: {pond}')
        # time.sleep(3)          
        step_count += 1
    print(f'\nSolved in {step_count} steps')


play(5)