from deep_find import deep_find


def deep_find_all(data, key):
    values = []
    value = None
    for data_key in data.keys():
        current_value = data[data_key]
        if data_key == key:
            values.append(current_value)
        else:
            if type(current_value) is dict:
                value = deep_find(current_value, key)
            if type(current_value) is list or type(current_value) is tuple:
                for el in current_value:
                    if type(el) is dict:
                        value = deep_find(el, key)
                    if value is not None:
                        values.append(value)
        if value is not None:
            values.append(value)
    return values
