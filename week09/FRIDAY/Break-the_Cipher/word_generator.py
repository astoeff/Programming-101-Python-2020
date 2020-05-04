from itertools import product
import string


def create_word_generator():
    syms = '.!<0123456789' + string.ascii_lowercase + string.ascii_uppercase
    word_generator = product(syms, repeat=5)
    return word_generator
