from playable import Playable

class Hero(Playable):
	def __init__(self, name, title, health, mana, mana_regeneration_rate):
		self.name = name
		self.title = title
		self.health = health
		self.mana = mana
		self.mana_regeneration_rate = mana_regeneration_rate
		self.weapon = None
		self.spell = None

	def known_as(self):
		return self.name + ' the ' + self.title

	def attack(self, **kwargs):
		result_from_attack = 0
		try:
			result_form_attack = super.attack(**kwargs)
		except Exception as e:
			raise e
		if result_form_attack != None:
			return result_form_attack
		return 0