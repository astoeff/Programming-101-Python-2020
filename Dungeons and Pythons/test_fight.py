import unittest


class TestFight(unittest.TestCase):
    def test_init_fiht(self):
        h = Hero(name="Bron", title="Dragonslayer",
                 health=100, mana=100, mana_regeneration_rate=2)


if __name__ == '__main__':
    unittest.main()
