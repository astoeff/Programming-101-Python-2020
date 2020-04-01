import unittest

from weapon import Weapon

class TestWeapon(unittest.TestCase):
    def test_init_weapon(self):
        name = "The Axe of Destiny"
        damage = 20

        w = Weapon(name=name, damage=damage)

        self.assertEqual(w.name, name)
        self.assertEqual(w.damage, damage)

if __name__ == '__main__':
    unittest.main()
