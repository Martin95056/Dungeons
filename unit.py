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
		try:
			self.curr_mana > spell.mana_cost
						
			self.curr_mana -= spell.mana_cost
			return True
		
		except:
			raise Exception("NOT ENOUGH MANA!!!")

	def take_damage(self, damage_points):
		if damage_points >= self.curr_health:
			self.curr_health = 0

		else:
			self.curr_health -= damage_points
		return self.curr_health

	def take_healing(self, healing_points):
		area = Dungeon('dungeon.txt')
		my_map = area._read_dungeon()

		if self.is_alive() == True:
			if my_map._pick_treasure() == 'health_potion':
				if self.health - self.curr_health > 100:
					self.curr_health += 100
		return self.curr_health

	def attack(self):
		return self.damage
