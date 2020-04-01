import unittest

from spell import Spell

class TestSpell(unittest.TestCase):
    def test_init_spell(self):
        name = "Fireball"
        damage = 30
        mana_cost = 50
        cast_range = 50

        s = Spell(name=name, damage=damage,\
         mana_cost=mana_cost, cast_range=cast_range)

        self.assertEqual(s.name, name)
        self.assertEqual(s.damage, damage)
        self.assertEqual(s.mana_cost, mana_cost)
        self.assertEqual(s.cast_range, cast_range)


if __name__ == '__main__':
    unittest.main()
