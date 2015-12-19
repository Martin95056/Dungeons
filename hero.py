from unit import Unit
from Dungeon import Dungeon


class Hero(Unit):
	def __init__(self, name, title, health, mana, mana_regen):
		self.name = name
		self.title = title
		self.mana_regen = mana_regen
		super().__init__(health, mana, 0)

		self.phisical_damage = 0
		self.magic_damage = 0

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

			self.damage = self.phisical_damage + weapon.damage
			self.max_equiped_weapons = 1
			return True

		else:
			print("{} cannot carry anymore weapons.".format(self.known_as()))
			return False

	def take_mana(self):
		area = Dungeon('dungeon.txt')
		my_map = area._read_dungeon()

		if my_map._move_hero() and (self.mana - self.curr_mana) > self.mana_regen:
			self.curr_mana += self.mana_regen

		elif my_map._pick_treasure() == 'mana_potion'
			if self.mana - self.curr_mana > 50:
				self.curr_mana += 50

		return self.curr_mana


	def learn(self, spell):
		if self.can_learn_spell():
			self.magic_damage = spell.damage
			self.max_learned_spells = 1
			return True
		else:
			print("{} cannot learn anymore magics.".format(self.known_as()))
			return False

	def can_attack(self):
		if self.max_equiped_weapons == 1 or self.max_learned_spells == 1:
			return True

		else:
			return False

	def attack(self, **kwargs):
		for key in kwargs:
			try:
				if key == 'by' and kwargs[key] == 'weapon':
					if self.can_attack() == True and self.phisical_damage != 0:
						self.damage += self.phisical_damage

					else:
						self.damage = self.damage

				elif key == 'by' and kwargs[key] == 'magic':
					if self.can_attack() == True and self.magic_damage != 0:
						self.damage = self.magic_damage

					else:
						self.damage = self.damage

				return self.damage

			except:
				raise Exception('for key use {} and for keyworld use {} or {}, please.'.format('by', 'weapon', 'magic'))
