import unittest
from enemy import Enemy
from spell import Spell
from weapon import Weapon


class TestEnemy(unittest.TestCase):
	def setUp(self):
		self.enemy = Enemy(200, 300, 50)

	def test_enemy_init(self):
		self.assertEqual(self.enemy.health, 200)
		self.assertEqual(self.enemy.mana, 300)

		self.assertEqual(self.enemy.curr_mana, self.enemy.mana)
		self.assertEqual(self.enemy.curr_health, self.enemy.health)

	def test_enemy_is_alive(self):
		self.enemy.curr_health = 30
		self.assertTrue(self.enemy.is_alive())

		self.enemy.curr_health = 0
		self.assertFalse(self.enemy.is_alive())

	def test_enemy_can_cast(self):
		s = Spell("BatkaAttack", 30, 50, 2)
		self.assertTrue(self.enemy.can_cast(s))
		self.assertEqual(self.enemy.curr_mana, 250)

		s1 = Spell("MegaBatkaAttack", 30, 350, 2)
		self.assertRaises(Exception)

	def test_enemy_take_damage(self):
		self.enemy.take_damage(50)
		self.assertEqual(self.enemy.curr_health, 150)

		self.enemy.take_damage(1000)
		self.assertEqual(self.enemy.curr_health, 0)

	def test_enemy_take_healing(self):
		self.assertFalse(self.enemy.take_healing(20))

		self.enemy.take_damage(100)
		self.assertTrue(self.enemy.take_healing(20))
		self.assertEqual(self.enemy.curr_health, 120)

		self.enemy.curr_health = 0
		self.assertFalse(self.enemy.take_healing(20))

	def test_enemy_attack(self):
		self.assertEqual(self.enemy.attack(), self.enemy.damage)


if __name__ == '__main__':
    unittest.main()
