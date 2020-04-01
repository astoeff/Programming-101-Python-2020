class Dungeon:
    def __init__(self, file):
        self.file = file
        self.map = self.to_string()
        self.validate_map()


    @classmethod
    def from_string(cls, string):
        with open("test.txt", 'w') as f:
            f.write(string)
        return cls(file="test.txt")


    def to_string(self):
        with open(self.file, 'r') as f:
            return f.read()


    def validate_map(self):
        assert 'S' in self.map, "No starting point"

        gates = 0
        for symbol in self.map:
            if symbol == "G":
                gates += 1
        assert gates == 1, "Number of gates != 1"
