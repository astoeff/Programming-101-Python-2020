from playable import Playable

class Enemy(Playable):
	def __init__(self, name, title, health, mana, damage):
		self.health = health
		self.mana = mana
		self.damage = damage
		self.weapon = None
		self.spell = None

	def attack(self, **kwargs):
		result_from_attack = 0
		try:
			result_form_attack = super.attack(**kwargs)
		except Exception as e:
			raise e
		if result_form_attack != None
			return result_form_attack
		return self.damage
		