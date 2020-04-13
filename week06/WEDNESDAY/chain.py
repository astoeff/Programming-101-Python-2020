# chain.py


def chain1(iterable_one, iterable_two):
    res = []
    for x in iterable_one:
        res.append(x)

    for x in iterable_two:
        res.append(x)

    return res


def chain2(iterable_one, iterable_two):
    res = []
    res.extend(iterable_one)
    res.extend(iterable_two)

    return res


def chain3(iterable_one, iterable_two):
    # TODO: If one is dict / not dict
    return [*iterable_one, *iterable_two]


def chain4(iterable_one, iterable_two):  # Not a good solution
    res = [*iterable_one, *iterable_two]

    for x in res:
        yield x


def chain5(iter1, iter2):  # Good solution!
    for x in iter1:
        yield x

    for x in iter2:
        yield x


iterable_one = range(4)
iterable_two = range(4, 10)

result = chain5(iterable_one, iterable_two)  # Good solution with generators.
# result = chain3(iterable_one, iterable_two)

print(result)
print(list(result))
