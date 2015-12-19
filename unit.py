from weapon import Weapon
from spell import Spell
from Dungeon import Dungeon


class Unit(object):
	def __init__(self, health, mana, damage):
		self.health = health
		self.mana = mana
		self.damage = damage

		self.curr_health = health
		self.curr_mana = mana

	def get_health(self):
		return self.curr_health

	def get_mana(self):
		return self.curr_mana
	
	def is_alive(self):
		return self.curr_health > 0

	def can_cast(self, spell):
		if self.curr_mana > spell.mana_cost:
			self.curr_mana -= spell.mana_cost
			return True
		
		else:
			print("Not enough mana.")
			return False

	def take_damage(self, damage_points):
		if damage_points >= self.curr_health:
			self.curr_health = 0
		else:
			self.curr_health -= damage_points

		return self.curr_health

	def take_healing(self, health_points):
		if self.is_alive():
			if self.health - self.curr_health >= health_points:
				self.curr_health += health_points

		return self.curr_health

	def attack(self):
		return self.damage
