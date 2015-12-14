from spell import Spell


class Unit:
	def __init__(self, health, mana):
		self.health = health
		self.mana = mana

		self.curr_health = 0
		self.curr_mana = 0

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
			return is_alive = False

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
