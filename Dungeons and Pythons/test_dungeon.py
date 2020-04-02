import unittest

from dungeon import Dungeon
from hero import Hero


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
        self.assertEqual(a.to_string("test.txt"), string)


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


    def test_spawn_hero_should_put_exactly_one_hero_on_the_map(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string('''
S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G
''')

        a.spawn(h)

        self.assertIn('H', a.map)


    def test_spawn_hero_with_no_more_spawning_points_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string('''
S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G
''')
        a.spawn(h)
        a.map = a.map.replace('H', 'T')

        spawned_successfully = a.spawn(h)

        self.assertFalse(spawned_successfully, "no starting points")


    def test_spawn_more_than_one_heroes_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string('''
S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G
''')
        a.spawn(h)

        spawned_successfully = a.spawn(h)

        self.assertFalse(spawned_successfully, "hero already spwaned!")


    def test_spawn_multiple_times(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string('''
S.##....ST
#T##..###.
#.###E###E
#.E..S###.
###T#####G
''')
        spawned_successfully1 = a.spawn(h)
        a.map = a.map.replace('H', 'T')
        spawned_successfully2 = a.spawn(h)
        a.map = a.map.replace('H', 'T')
        spawned_successfully3 = a.spawn(h)

        self.assertTrue(spawned_successfully1, "cannot spawn")
        self.assertTrue(spawned_successfully2, "cannot spawn")
        self.assertTrue(spawned_successfully3, "cannot spawn")



if __name__ == '__main__':
    unittest.main()
