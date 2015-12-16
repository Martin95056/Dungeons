from unit import Unit


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

	def take_mana(self, mana_points):
		if map.move_hero():
			if (self.get_mana() + self.mana_regen) < self.mana:
				self.get_mana() += self.mana_regen

		else:
			if (self.get_mana() + mana_points) < self.mana:
				self.get_mana() += mana_points

		return self.get_mana()

	def learn(self, spell):
		if self.can_learn_spell():

			self.magic_damage = spell.damage
			self.max_learned_spells = 1
			return Tru
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
