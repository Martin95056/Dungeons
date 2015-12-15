from hero import Hero


class Enemy(Hero):
	def __init__(self, health, mana, damage):
		self.damage = damage
		super().__init__(health, mana)
