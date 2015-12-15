from enemy import Enemy


class Hero(Enemy):
	def __init__(self, name, title, health, mana, mana_regen):
		self.name = name
		self.title = title
		self.mana_regen = mana_regen
		super().__init__(health, mana, 0)

	def known_as(self):
		return "{} the {}".format(self.name, self.title)
