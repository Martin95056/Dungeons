from enemy import Enemy
from spell import Spell
from weapon import Weapon


class Hero(Enemy):

    def __init__(self, name, title, health, mana, mana_regen):
        self.name = name
        self.title = title
        self.mana_regen = mana_regen
        self._max_equiped_weapons = 0
        self._max_learned_spells = 0
        super().__init__(health, mana, 0)


    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def can_equip(self):
        return self._max_equiped_weapons == 0

    def can_learn_spell(self):
        return self._max_learned_spells == 0

    def equip(self, weapon):
        if self.can_equip():
            self.damage = self.phisical_damage + weapon.damage
            self._max_equiped_weapons = 1
            print(self.known_as()+" equiped "+ str(weapon))
            return True


        else:
            print(
                "{} cannot carry anymore weapons.".format(self.known_as()))
            return False

    def learn(self, spell):
        if self.can_learn_spell():
            self.magic_damage = spell.damage
            self._max_learned_spells = 1
            print(self.known_as() + " learned " + str(spell))
            return True

        else:
            print(
                "{} cannot learn anymore magics.".format(self.known_as()))
            return False


h = Hero(name='Mincho', title='Tupiq', health=100, mana=100, mana_regen=2)
s = Spell(name='kdak', damage=20, mana_cost=20, cast_range=10)
s2 = Spell(name='kdak', damage=20, mana_cost=20, cast_range=10)
h.learn(s)
h.learn(s2)
