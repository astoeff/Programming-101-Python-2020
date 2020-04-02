class Dungeon:
    def __init__(self, file):
        self.map = self.to_string(file)
        self.validate_map()


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
