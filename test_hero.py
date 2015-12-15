import unittest
from hero import Hero
from spell import Spell
from weapon import Weapon



class TestHero(unittest.TestCase):
	def setUp(self):
		self.hero = Hero("Martin", "Manqk", 200, 300, 3)

	def test_hero_init(self):
		self.assertEqual(self.hero.name, "Martin")
		self.assertEqual(self.hero.title, "Manqk")
		self.assertEqual(self.hero.health, 200)
		self.assertEqual(self.hero.mana, 300)
		self.assertEqual(self.hero.mana_regen, 3)

		self.assertEqual(self.hero.curr_mana, self.hero.mana)
		self.assertEqual(self.hero.curr_health, self.hero.health)

	def test_hero_known_as(self):
		self.assertEqual(self.hero.known_as(), "Martin the Manqk")

	def test_hero_is_alive(self):
		self.hero.curr_health = 30
		self.assertTrue(self.hero.is_alive())

		self.hero.curr_health = 0
		self.assertFalse(self.hero.is_alive())

	def test_hero_can_cast(self):
		s = Spell("BatkaAttack", 30, 50, 2)
		self.assertTrue(self.hero.can_cast(s))
		self.assertEqual(self.hero.curr_mana, 250)

		s1 = Spell("MegaBatkaAttack", 30, 350, 2)
		self.assertRaises(Exception)

	def test_hero_take_damage(self):
		self.hero.take_damage(50)
		self.assertEqual(self.hero.curr_health, 150)

		self.hero.take_damage(1000)
		self.assertEqual(self.hero.curr_health, 0)

	def test_hero_take_healing(self):
		self.assertFalse(self.hero.take_healing(20))

		self.hero.take_damage(100)
		self.assertTrue(self.hero.take_healing(20))
		self.assertEqual(self.hero.curr_health, 120)

		self.hero.curr_health = 0
		self.assertFalse(self.hero.take_healing(20))

	def test_hero_equip(self):
		w = Weapon('noj', 20)
		self.hero.equip(w)
		self.assertEqual(self.hero.phisical_damage, w.damage)
		self.assertEqual(self.hero.max_equiped_weapons, 1)

		self.assertRaises(Exception)

	def test_hero_learn(self):
		s = Spell("BatkaAttack", 30, 50, 2)
		self.hero.learn(s)
		self.assertEqual(self.hero.magic_damage, s.damage)
		self.assertEqual(self.hero.max_learned_spells, 1)

		self.assertRaises(Exception)

	def test_hero_attack(self):
		w = Weapon('noj', 20)
		self.hero.equip(w)
		self.hero.attack(by='weapon')
		self.assertTrue(self.hero.can_attack())
		self.assertEqual(self.hero.damage, self.hero.phisical_damage)

		s = Spell("BatkaAttack", 30, 50, 2)
		self.hero.learn(s)
		self.hero.attack(by='magic')
		self.assertEqual(self.hero.damage, self.hero.magic_damage)

		self.hero.attack(by='phisical damage')
		self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main()
