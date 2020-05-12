from functools import wraps


def debug(func):
    fname = func.__qualname__

    @wraps(func)
    def wrapper(*arg, **kwargs):
        print('Calling {}'.format(fname))

        return func(*arg, **kwargs)

    return wrapper


def debugmethods(cls):
    for attr, value in vars(cls).items():
        if callable(value):
            setattr(cls, attr, debug(value))

    return cls


class MyType(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        clsobj = debugmethods(clsobj)
        return clsobj
