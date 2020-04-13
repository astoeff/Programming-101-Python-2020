class NumberIterator:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        index = self.index
        self.index += 1
        try:
            return self.values[index]
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    i = NumberIterator()
    iter(i)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
