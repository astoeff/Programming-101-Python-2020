import unittest

from dungeon import Dungeon
from hero import Hero


class TestDungeon(unittest.TestCase):
    def test_validate_map_with_correct_input(self):
        string = (
'''S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G'''
)

        a = Dungeon.from_string(string)

        self.assertIsInstance(a, Dungeon)
        self.assertEqual(a.to_string("test.txt"), string)


    def test_to_list(self):
        string = (
'''S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        expected = (
[['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'],
 ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'],
 ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'],
 ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'],
 ['#', '#', '#', 'T', '#', '#','#', '#', '#', 'G']]
)

        a = Dungeon.from_string(string)

        self.assertEqual(expected, a.list_map)


    def test_validate_map_with_no_starting_point_should_raise_error(self):
        with self.assertRaises(AssertionError):
            a = Dungeon.from_string(
'''T.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G'''
)


    def test_validate_map_with_more_than_one_gates(self):
        with self.assertRaises(AssertionError):
            a = Dungeon.from_string(
'''S.##.....T
#G##..###.
#.###E###E
#.E...###.
###T#####G'''
)


    def test_spawn_hero_should_put_exactly_one_hero_on_the_map(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G'''
)

        a.spawn(h)

        self.assertIn('H', a.map)


    def test_spawn_hero_with_no_more_spawning_points_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)
        a.map = a.map.replace('H', 'T')

        spawned_successfully = a.spawn(h)

        self.assertFalse(spawned_successfully, "no starting points")


    def test_spawn_more_than_one_heroes_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)

        spawned_successfully = a.spawn(h)

        self.assertFalse(spawned_successfully, "hero already spwaned!")


    def test_spawn_multiple_times(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##....ST
#T##..###.
#.###E###E
#.E..S###.
###T#####G'''
)
        spawned_successfully1 = a.spawn(h)
        a.map = a.map.replace('H', 'T')
        spawned_successfully2 = a.spawn(h)
        a.map = a.map.replace('H', 'T')
        spawned_successfully3 = a.spawn(h)

        self.assertTrue(spawned_successfully1, "cannot spawn")
        self.assertTrue(spawned_successfully2, "cannot spawn")
        self.assertTrue(spawned_successfully3, "cannot spawn")




class TestMoveHero(unittest.TestCase):
    def test_move_hero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##.....T
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)

        moved_successfully = a.move_hero('right')

        self.assertTrue(moved_successfully, "cannot move")


    def test_move_hero_with_right_next_to_the_wall_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''T.##.....S
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)

        moved_successfully = a.move_hero('right')

        self.assertFalse(moved_successfully, "got out of the map")


    def test_move_hero_with_right_should_move_the_hero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##.....T
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        expected = (
'''.H##.....T
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)

        a.move_hero('right')

        self.assertEqual(expected, a.map)


    def test_move_hero_with_left_should_move_the_hero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##.....T
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        expected = (
'''H.##.....T
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)
        a.move_hero('right')

        a.move_hero('left')

        self.assertEqual(expected, a.map)


    def test_move_hero_with_left_next_to_the_wall_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##.....T
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)

        moved_successfully = a.move_hero('left')

        self.assertFalse(moved_successfully, "got out of the map")


    def test_move_hero_with_up_should_move_the_hero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''..##.....T
.S##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        expected = (
'''.H##.....T
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)
        a.move_hero('left')
        a.move_hero('right')

        a.move_hero('up')

        self.assertEqual(expected, a.map)


    def test_move_hero_with_up_next_to_the_wall_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''S.##.....T
..##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)

        moved_successfully = a.move_hero('up')

        self.assertFalse(moved_successfully, "got out of the map")


    def test_move_hero_with_down_should_move_the_hero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''..##.....T
.S##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        expected = (
'''..##.....T
.H##..###.
#.###E###E
#.E...###.
###T#####G'''
)
        a.spawn(h)
        a.move_hero('left')
        a.move_hero('right')
        a.move_hero('up')

        a.move_hero('down')

        self.assertEqual(expected, a.map)


    def test_move_hero_with_down_next_to_the_wall_should_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''..##.....T
..##..###.
#.###E###E
#.ES..###.
###.#####G'''
)
        a.spawn(h)
        a.move_hero('down')

        moved_successfully = a.move_hero('down')

        self.assertFalse(moved_successfully, "got out of the map")


    def test_move_onto_an_obstacle_returns_false_but_others_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        a = Dungeon.from_string(
'''..##.....T
..##..###.
#.###E###E
#.ES..###.
###.#####G'''
)
        a.spawn(h)

        moved_successfully1 = a.move_hero('down')
        moved_successfully2 = a.move_hero('right')
        moved_successfully3 = a.move_hero('left')
        moved_successfully4 = a.move_hero('up')
        moved_successfully5 = a.move_hero('right')
        moved_successfully6 = a.move_hero('right')
        moved_successfully7 = a.move_hero('right')


        self.assertTrue(moved_successfully1, "cannot move")
        self.assertFalse(moved_successfully2, "got onto an obstacle")
        self.assertFalse(moved_successfully3, "got onto an obstacle")
        self.assertTrue(moved_successfully4, "cannot move")
        self.assertTrue(moved_successfully5, "cannot move")
        self.assertTrue(moved_successfully6, "cannot move")
        self.assertFalse(moved_successfully7, "got onto an obstacle")


if __name__ == '__main__':
    unittest.main()
