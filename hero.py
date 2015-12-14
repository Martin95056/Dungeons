from unit import Unit
from weapon import Weapon
from spell import Spell


class Hero(Unit):
	def __init__(self, name, title, mana_regen, health, mana):
		super(Unit, self).__init__(health, mana)

		self.name = name
		self.title = title
		self.mana_regen = mana_regen

		self.phisical_damage = 0
		self.magic_damage = 0
		self.damage = 0

		self.max_equiped_weapons = 0
		self.max_learned_spells = 0

	def known_as(self):
		return "{} the {}".format(self.name, self.title)

	def can_equip(self):
		return self.max_equiped_weapons == 0

	def can_learn_spell(self):
		return self.max_learned_spells == 0

	def equip(self, weapon):
		try:
			self.can_equip()

			self.phisical_damage = weapon.damage
			self.max_equiped_weapons = 1

		except:
			print("{} cannot carry anymore weapons.".format(self.known_as())

	def learn(self, spell):
		try:
			self.can_learn_spell()

			self.magic_damage = spell.damage
			self.max_learned_spells = 1

		except:
			print("{} cannot learn anymore magics.".format(self.known_as())

	def can_attack(self):
		if self.max_equiped_weapons == 0 and self.max_learned_spells ==0:
			return True

		else:
			return False

	def attack(self, **kwargs):
		for key in kwargs:

			try:
				key == 'by' and kwargs[key] == 'weapon'
				if self.can_attack() == True and self.phisical_damage != 0:
					self.damage = self.phisical_damage

				else:
					self.damage = 0

			elif key == 'by' and kwargs[key] == 'magic':
				if self.can_attack() == True and self.magic_damage != 0:
					self.damage = self.magic_damage

				else:
					self.damage = 0

				return self.damage

			except:
				raise Exception('for key use {} and for keyworld use {} or {}, please.'.format('by', 'weapon', 'magic'))
