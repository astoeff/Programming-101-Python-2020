import unittest
from hero import Hero

class TestHero(unittest.TestCase):
	#__init__()
	def test_with_given_correct_arguments_should_initialise_hero(self):
		name = 'Bron'
		title = 'Dragonslayer'
		health = 100
		mana = 100
		mana_regeneration_rate = 2

		h = Hero(name, title, health, mana, mana_regeneration_rate)

		self.assertEqual(Hero, type(h))
		self.assertEqual(name, h.name)
		self.assertEqual(title, h.title)
		self.assertEqual(health, h.health)
		self.assertEqual(mana_regeneration_rate, h.mana_regeneration_rate)

	#known_as()
	def test_with_given_hero_should_return_correctly(self):
		name = 'Bron'
		title = 'Dragonslayer'
		health = 100
		mana = 100
		mana_regeneration_rate = 2
		h = Hero(name, title, health, mana, mana_regeneration_rate)

		result = h.known_as()
		expected = name + ' the ' + title

		self.assertEqual(expected, result)

if __name__ == '__main__':
	unittest.main()