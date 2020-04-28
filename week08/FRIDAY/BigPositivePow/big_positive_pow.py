from random import randint


def big_positive_pow():
    x = randint(100, 10000)
    y = randint(-10, 100)

    if y < 1:
        raise ValueError('Try again.')

    return x ** y
