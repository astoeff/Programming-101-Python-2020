from functools import wraps


def debug(func):  #function decorator
    fname = func.__qualname__

    @wraps(func)
    def wrapper(*arg, **kwargs):
        print('Calling {}'.format(fname))

        return func(*arg, **kwargs)

    return wrapper


def debugmethods(cls):  #class decorator
    for attr, value in vars(cls).items():
        if callable(value):
            setattr(cls, attr, debug(value))

    return cls


class MyType(type):  #hierarchy decorator
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        clsobj = debugmethods(clsobj)
        return clsobj
