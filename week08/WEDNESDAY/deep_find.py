#from collections.abc import Iterable   # drop `.abc` with Python 2.7 or lower


# def is_iterable(obj):
#     return isinstance(obj, Iterable)


def deep_find(data, key):
    value = None
    for data_key in data.keys():
        current_value = data[data_key]
        if data_key == key:
            return current_value
        else:
            if type(current_value) is dict:
                value = deep_find(current_value, key)
            if type(current_value) is list or type(current_value) is tuple:
                for el in current_value:
                    if type(el) is dict:
                        value = deep_find(el, key)
                    if value is not None:
                        return value
        if value is not None:
            return value
    return value


if __name__ == '__main__':
    x = {'gosho': 20, 'pesho': [2, 100], 'men': {'y': 200.3, 'x': 1000}}
    y = {'gosho': 20, 'pesho': [2, 100], 'men': [{'y': 200.3, 'x': 1000}, {'z': 21, 'result': 42}]}
    z = {'gosho': [20, {'x': 200, 'y': 500}, [{'p': 12, 'a': 100}, ({'o': 2, 'k': 21})]], 'm': 22}
    print(deep_find(x, 'x'))
    print(deep_find(y, 'result'))
    print(deep_find(z, 'k'))
