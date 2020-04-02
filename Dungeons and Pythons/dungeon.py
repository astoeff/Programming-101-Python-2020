class Dungeon:
    def __init__(self, file):
        self.list_map = [[]]
        self.map = self.to_string(file)
        self.validate_map()
        self.to_list()


    @classmethod
    def from_string(cls, string):
        with open("test.txt", 'w') as f:
            f.write(string)
        return cls(file="test.txt")


    def to_string(self, file):
        with open(file, 'r') as f:
            return f.read()


    def validate_map(self):
        assert 'S' in self.map, "No starting point"

        gates = 0
        for symbol in self.map:
            if symbol == "G":
                gates += 1
        assert gates == 1, "Number of gates != 1"


    def print_map(self):
        print(self.map)


    def spawn(self, hero):
        if 'H' in self.map:
            return False
        if 'S' in self.map:
            self. map = self.map.replace('S', 'H', 1)
            return True
        else:
            return False


    # def move_hero(self, direction):
    #     current_position = self.map.index('H')



    def to_list(self):
        i = 0
        for symbol in self.map:
            if symbol == '\n':
                self.list_map.append([])
                i += 1
            else:
                self.list_map[i].append(symbol)
        # with open(file, 'r') as f:
        #     i = 0
        #     for line in f.readlines():
        #         self.map.append([])
        #         for symbol in line:
        #             if symbol != '\n':
        #                 self.map[i].append(symbol)
        #         i += 1
