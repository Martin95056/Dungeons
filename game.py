from dungeon import Dungeon
from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell


def main():

    hero = Hero('Garen', 'King', 300, 200, 2)
    enemy = Enemy(100, 100, 50)

    axe = Weapon('Bloody Axe', 40)
    fireball = Spell('Fireball', 30, 50, 2)

    hero.learn(fireball)
    hero.equip(axe)

    forest = Dungeon('dungeon.txt')

    #Iztrih komandite, no vsichko e OK. Heroto se mardashe po mapa i kato se sbiqt, fight.txt se palneshe.

if __name__ == '__main__':
    main()