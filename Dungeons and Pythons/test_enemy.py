import unittest
from constants import PLAYER_ATTACK_BY_WEAPON_STRING, PLAYER_ATTACK_BY_SPELL_STRING
from enemy import Enemy
from weapon import Weapon
from spell import Spell

class TestEnemy(unittest.TestCase):
	#__init__()
	def test_with_given_correct_arguments_should_initialise_enemy(self):
		health = 100
		mana = 100
		damage = 20

		e = Enemy(health, mana, damage)

		self.assertEqual(Enemy, type(e))
		self.assertEqual(health, e.health)
		self.assertEqual(mana, e.mana)
		self.assertEqual(damage, e.damage)

	#attack(by)
	def test_with_given_enemy_and_invalid_by_as_argument_should_raise_exception(self):
		health = 100
		mana = 100
		damage = 20

		e = Enemy(health, mana, damage)
		by = None

		exc = None
		try:
			e.attack(by=by)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid item for attack given')

	def test_with_given_enemy_with_no_weapon_and_weapon_as_argument_should_return_zero(self):
		health = 100
		mana = 100
		damage = 20

		e = Enemy(health, mana, damage)
		by = PLAYER_ATTACK_BY_WEAPON_STRING
			
		result = e.attack(by=by)
			
		self.assertEqual(0, result)

	def test_with_given_enemy_with_weapon_and_weapon_as_argument_should_return_damage_of_weapon(self):
		health = 100
		mana = 100
		damage = 20

		e = Enemy(health, mana, damage)
		weapon = Weapon(name='Fireball', damage=30)	
		e.equip(weapon)
		by = PLAYER_ATTACK_BY_WEAPON_STRING
			
		result = e.attack(by=by)
			
		self.assertEqual(30, result)

	def test_with_given_enemy_with_no_spell_and_spell_as_argument_should_return_zero(self):
		health = 100
		mana = 100
		damage = 20

		e = Enemy(health, mana, damage)
		by = PLAYER_ATTACK_BY_SPELL_STRING
			
		result = e.attack(by=by)
			
		self.assertEqual(0, result)

	def test_with_given_enemy_with_castable_spell_and_spell_as_argument_should_return_damage_of_spell(self):
		health = 100
		mana = 100
		damage = 20

		e = Enemy(health, mana, damage)
		spell = Spell(name='Fireball', damage=30, mana_cost=50, cast_range=2)
		e.learn(spell)
		by = PLAYER_ATTACK_BY_SPELL_STRING
			
		result = e.attack(by=by)
			
		self.assertEqual(30, result)

	def test_with_given_enemy_with_non_castable_spell_and_spell_as_argument_should_return_zerol(self):
		health = 100
		mana = 20
		damage = 20

		e = Enemy(health, mana, damage)
		spell = Spell(name='Fireball', damage=30, mana_cost=50, cast_range=2)
		e.learn(spell)
		by = PLAYER_ATTACK_BY_SPELL_STRING
			
		result = e.attack(by=by)
			
		self.assertEqual(0, result)

	def test_with_given_enemy_with_no_item_for_attack_should_return_damage_of_enemy(self):
		health = 100
		mana = 100
		damage = 30

		e = Enemy(health, mana, damage)		
			
		result = e.attack()
			
		self.assertEqual(damage, result)

if __name__ == '__main__':
	unittest.main()