import unittest

from dungeon import Dungeon


class TestDungeon(unittest.TestCase):
    def test_validate_map_with_correct_input(self):
        string = '''
S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G
'''

        a = Dungeon.from_string(string)

        self.assertIsInstance(a, Dungeon)
        self.assertEqual(a.file, "test.txt")
        self.assertEqual(a.to_string(), string)


    def test_validate_map_with_no_starting_point_should_raise_error(self):
        with self.assertRaises(AssertionError):
            a = Dungeon.from_string('''
T.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G
''')


    def test_validate_map_with_more_than_one_gates(self):
        with self.assertRaises(AssertionError):
            a = Dungeon.from_string('''
S.##.....T
#G##..###.
#.###E###E
#.E...###.
###T#####G
''')


if __name__ == '__main__':
    unittest.main()
