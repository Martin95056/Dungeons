from unit import Unit
from weapon import Weapon
from spell import Spell


class Hero(Unit):
	def __init__(self, name, title, mana_regen, health, mana):
		super(Unit, self).__init__(health, mana)

		self.name = name
		self.title = title
		self.mana_regen = mana_regen

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
		if self.can_equip():
			self.damage = weapon.damage
			self.max_equiped_weapons = 1

		else:
			print("{} cannot carry anymore weapons.".format(self.known_as())

	def can_cast(self):
		super(Unit, self).can_cast()




