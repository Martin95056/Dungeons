from weapon import Weapon
from spell import Spell


class Hero():
	def __init__(self, name, title, health, mana,  mana_regen):
		self.name = name
		self.title = title
		self.health = health
		self.mana = mana
		self.mana_regen = mana_regen

		self.curr_health = 0
		self.curr_mana = 0

		self.phisical_damage = 0
		self.magic_damage = 0
		self.damage = 0

		self.max_equiped_weapons = 0
		self.max_learned_spells = 0

	def known_as(self):
		return "{} the {}".format(self.name, self.title)

	def is_alive(self):
		return self.curr_health > 0

	def can_cast(self):
		try:
			self.curr_mana > spell.mana_cost
						
			self.curr_mana -= spell.mana_cost
			return True
		
		except:
			print("NOT ENOUGH MANA!!!")

	def get_health(self):
		return self.curr_health

	def get_mana(self):
		return self.curr_mana

	def take_damage(self, damage_points):
		if damage_points >= self.curr_health:
			self.curr_health = 0

		else:
			self.curr_health -= damage_points
		return self.curr_health

	def take_healing(healing_points):
		if self.is_alive() == True:
			if (selh.curr_health + healing_points) <= self.health:
				self.curr_health += healing_points
				return True

			else:
				pass
		else:
			return False

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
			print("{} cannot carry anymore weapons.".format(self.known_as()))

	def learn(self, spell):
		try:
			self.can_learn_spell()

			self.magic_damage = spell.damage
			self.max_learned_spells = 1

		except:
			print("{} cannot learn anymore magics.".format(self.known_as()))

	def can_attack(self):
		if self.max_equiped_weapons == 0 and self.max_learned_spells == 0:
			return True

		else:
			return False

	def attack(self, **kwargs):
		for key in kwargs:

			try:
				if key == 'by' and kwargs[key] == 'weapon':
					if self.can_attack() == True and self.phisical_damage != 0:
						self.damage = self.phisical_damage

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
