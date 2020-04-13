class Pandas:
    def __init__(self):
        self.data = [
            {'name': 'Ivo', 'kg': 100},
            {'name': 'Marto', 'kg': 80},
            {'name': 'Pesho', 'kg': 120}
        ]

    def __iter__(self):
        self.index = 0
        return self  # Important!

    def __next__(self):
        index = self.index
        self.index += 1

        try:
            return self.data[index]
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    pandas = Pandas()
    for panda in pandas:
        print(panda)
