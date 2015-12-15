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

	def test_enemy_equip(self):
		w = Weapon('noj', 20)
		self.enemy.equip(w)
		self.assertEqual(self.enemy.damage, self.enemy.phisical_damage + w.damage)
		self.assertEqual(self.enemy.max_equiped_weapons, 1)

		self.assertRaises(Exception)

	def test_enemy_learn(self):
		s = Spell("BatkaAttack", 30, 50, 2)
		self.enemy.learn(s)
		self.assertEqual(self.enemy.magic_damage, s.damage)
		self.assertEqual(self.enemy.max_learned_spells, 1)

		self.assertRaises(Exception)

	def test_enemy_attack(self):
		self.enemy.attack(by='MMA')
		self.assertEqual(self.enemy.damage, 50)

		w = Weapon('noj', 20)
		self.enemy.equip(w)
		self.enemy.attack(by='weapon')
		self.assertTrue(self.enemy.can_attack())
		self.assertEqual(self.enemy.damage, self.enemy.phisical_damage + self.enemy.damage)

		s = Spell("BatkaAttack", 30, 50, 2)
		self.enemy.learn(s)
		self.enemy.attack(by='magic')
		self.assertEqual(self.enemy.damage, self.enemy.magic_damage)

		self.enemy.attack(by='RKO')
		self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main()
