import constants


class Pond():
    def __init__(self, frogs_per_side):
        assert frogs_per_side >= 0, 'Enter non-negative number of frogs per side'
        self.frogs_per_side = frogs_per_side
        self.pond_size = frogs_per_side * 2 + 1
        self.steps_count = 0
        self.free_lilly_position = self.pond_size // 2
        self.leftside_frogs_final_position = self.pond_size - 1
        self.rightside_frogs_final_position = 0

    def set_pond_string(self):
        pond = ''
        for pos in range(0, self.free_lilly_position):
            pond += constants.LEFT_FROG_SYMMBOL

        pond += constants.FREE_LILLY_SYMBOL

        for pos in range(0, self.free_lilly_position):
            pond += constants.RIGHT_FROG_SYMBOL

        self.pond_string = pond
        self.pond_arranged = pond[::-1]

    def is_arranged(self):
        return self.pond_string == self.pond_arranged

    def __repr__(self):
        return f'Step {self.steps_count}: {self.pond_string}'

    def convert_pond_string_to_array(self):
        return list(self.pond_string)

    def move_leftside_frog(self):
        result_from_move = False
        pond_as_array = self.convert_pond_string_to_array()

        if self.free_lilly_position == self.leftside_frogs_final_position:
            pond_as_array[self.free_lilly_position] = constants.LEFT_FROG_SYMMBOL

            position_of_leftside_frog = self.free_lilly_position - 1

            if pond_as_array[position_of_leftside_frog] != constants.LEFT_FROG_SYMMBOL:
                position_of_leftside_frog -= 1

            pond_as_array[position_of_leftside_frog] = constants.FREE_LILLY_SYMBOL
            self.pond_string = ''.join(pond_as_array)
            self.leftside_frogs_final_position -= 1
            self.free_lilly_position = position_of_leftside_frog
            result_from_move = True

        elif self.free_lilly_position == 1:
            matching_value = constants.LEFT_FROG_SYMMBOL + constants.FREE_LILLY_SYMBOL + constants.RIGHT_FROG_SYMBOL
            cuurrent_condition_for_moving_leftside_frog = self.pond_string[0:3] == matching_value
            if cuurrent_condition_for_moving_leftside_frog:
                pond_as_array[self.free_lilly_position] = constants.LEFT_FROG_SYMMBOL
                pond_as_array[self.free_lilly_position - 1] = constants.FREE_LILLY_SYMBOL
                self.pond_string = ''.join(pond_as_array)
                self.free_lilly_position -= 1
                result_from_move = True

        elif self.free_lilly_position >= 2:
            first_matching_value = constants.LEFT_FROG_SYMMBOL + constants.LEFT_FROG_SYMMBOL + constants.FREE_LILLY_SYMBOL + constants.RIGHT_FROG_SYMBOL
            second_matching_value = constants.LEFT_FROG_SYMMBOL + constants.RIGHT_FROG_SYMBOL + constants.FREE_LILLY_SYMBOL + constants.RIGHT_FROG_SYMBOL
            pond_range_to_check = self.pond_string[self.free_lilly_position - 2: self.free_lilly_position + 2]

            first_condition_for_moving_leftside_frog = pond_range_to_check == first_matching_value
            second_condition_for_moving_leftside_frog = pond_range_to_check == second_matching_value

            if first_condition_for_moving_leftside_frog:
                pond_as_array[self.free_lilly_position] = constants.LEFT_FROG_SYMMBOL
                pond_as_array[self.free_lilly_position - 1] = constants.FREE_LILLY_SYMBOL
                self.pond_string = ''.join(pond_as_array)
                self.free_lilly_position -= 1
                result_from_move = True
            elif second_condition_for_moving_leftside_frog:
                pond_as_array[self.free_lilly_position] = constants.LEFT_FROG_SYMMBOL
                pond_as_array[self.free_lilly_position - 2] = constants.FREE_LILLY_SYMBOL
                self.pond_string = ''.join(pond_as_array)
                self.free_lilly_position -= 2
                result_from_move = True

        if result_from_move:
            self.steps_count += 1

        return result_from_move

    def move_rightside_frog(self):
        pond_as_array = self.convert_pond_string_to_array()
        position_of_rightside_frog = self.free_lilly_position + 1

        if pond_as_array[position_of_rightside_frog] != constants.RIGHT_FROG_SYMBOL:
            position_of_rightside_frog += 1

        pond_as_array[position_of_rightside_frog] = constants.FREE_LILLY_SYMBOL
        pond_as_array[self.free_lilly_position] = constants.RIGHT_FROG_SYMBOL
        self.pond_string = ''.join(pond_as_array)
        self.free_lilly_position = position_of_rightside_frog
        self.steps_count += 1

    def move_frog(self):
        if not self.move_leftside_frog():
            self.move_rightside_frog()
