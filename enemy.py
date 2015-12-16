from unit import Unit


class Enemy(Unit):
	def __init__(self, health, mana, damage):
		super().__init__(health, mana, damage)
