def cycle(iterable):
    while True:
        for el in iterable:
            yield el


if __name__ == '__main__':
    endless = cycle(range(0, 10))
    # for i in range(0, 21):
    #     print(next(endless))
    # for item in endless:
    #     print(item)
    # print(list(endless))
