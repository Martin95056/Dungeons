import unittest
from hero import Hero
from spell import Spell
from weapon import Weapon


class TestHero(unittest.TestCase):
	def setUp(self):
		self.hero = Hero("Martin", "Manqk", 200, 300, 3)

	def test_hero_init_(self):
		self.assertEqual(self.hero.health, 200)
		self.assertEqual(self.hero.mana, 300)
		self.assertEqual(self.hero.damage, 0)

		self.assertEqual(self.hero.name, "Martin")
		self.assertEqual(self.hero.title, "Manqk")
		self.assertEqual(self.hero.mana_regen, 3)

	def test_hero_known_as(self):
		self.assertEqual(self.hero.known_as(), "Martin the Manqk")

	def test_hero_attack(self):
		self.hero.attack(by='MMA')
		self.assertEqual(self.hero.damage, 0)

		w = Weapon('noj', 20)
		self.hero.equip(w)
		self.hero.attack(by='weapon')
		self.assertTrue(self.hero.can_attack())
		self.assertEqual(self.hero.damage, self.hero.phisical_damage + self.hero.damage)

		s = Spell("BatkaAttack", 30, 50, 2)
		self.hero.learn(s)
		self.hero.attack(by='magic')
		self.assertEqual(self.hero.damage, self.hero.magic_damage)

		self.hero.attack(by='RKO')
		self.assertRaises(Exception)

#testing only attack() methhod because others are similar ot the Enemy's
if __name__ == '__main__':
    unittest.main()
