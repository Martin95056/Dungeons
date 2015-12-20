from random import randint
from spell import Spell
from hero import Hero
from enemy import Enemy
from weapon import Weapon


class Dungeon:
    def __init__(self, filename):
        self._filename = filename
        self._is_found = False

        self.hero_x = 0
        self.hero_y = 0

    def _read_dungeon(self):
        dungeon = [[]]
        with open(self._filename, 'r') as data:
            dungeon = [list(item) for line in data for item in line.split()]
        
        return dungeon

    def _write_dungeon(self, dungeon):
        data = open(self._filename, 'w')
        for item in dungeon:
            data.write(''.join(item)+"\n")

    def _print_map(self):
        my_list = []
        dungeon_map = self._read_dungeon()
        for row in range(0, len(dungeon_map)):
            for col in range(0, len(dungeon_map[row])):
                my_list.append(dungeon_map[row][col])
            print(''.join(my_list))
            my_list = []


    def _spawn(self, hero):
        dungeon = self._read_dungeon()
        for row in range(0, len(dungeon)):
            for col in range(0, len(dungeon[row])):
                if dungeon[row][col] == 'S':
                    dungeon[row][col] = 'H'
                    self.hero_x = row
                    self.hero_y = col
        
        self._write_dungeon(dungeon)

    def _move_up(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if self.hero_x == 0 or my_map[self.hero_x - 1][self.hero_y] == '#':
                    print("Your hero cannot move up.")
                    return False

                else:
                    my_map[self.hero_x][self.hero_y] = '.'
                    my_map[self.hero_x - 1][self.hero_y] = 'H'
                    self.hero_x -= 1
                    self._write_dungeon(my_map)
                    return True

    def _move_down(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if self.hero_x == len(my_map) or my_map[self.hero_x + 1][self.hero_y] == '#':
                    print("Your hero cannot move down.")
                    return False

                else:
                    my_map[self.hero_x][self.hero_y] = '.'
                    my_map[self.hero_x + 1][self.hero_y] = 'H'
                    self.hero_x += 1
                    self._write_dungeon(my_map)
                    return True

    def _move_right(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if self.hero_y == len(my_map[row]) or my_map[self.hero_x][self.hero_y + 1] == '#':
                    print("Your hero cannot move right.")
                    return False

                else:
                    my_map[self.hero_x][self.hero_y] = '.'
                    my_map[self.hero_x][self.hero_y + 1] = 'H'
                    self.hero_y += 1
                    self._write_dungeon(my_map)
                    return True

    def _move_left(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if self.hero_y == 0 or my_map[self.hero_x][self.hero_y - 1] == '#':
                    print("Your hero cannot move left.")
                    return False

                else:
                    my_map[self.hero_x][self.hero_y] = '.'
                    my_map[self.hero_x][self.hero_y - 1] = 'H'
                    self.hero_y -= 1
                    self._write_dungeon(my_map)
                    return True

    def _move_hero(self, *args):
        for direction in args:
            if direction == 'up':
                self._move_up()
            elif direction == 'down':
                self._move_down()
            elif direction == 'right':
                self._move_right()
            elif direction == 'left':
                self._move_left()
                return True

            else:
                raise Exception("Valid directions are up, down, right and left.")
                return False

    def _read_treasures(self):
        filename = 'treasures.txt'
        with open(filename, 'r') as data:
            treasures = [item for line in data for item in line.split()]
        return treasures

    def _pick_treasure(self):
        treasures = self._read_treasures()
        num = randint(0, len(treasures)-1)

        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'T':
                    if treasures[num] == 'health_potion':
                        print("You have found a health potion.")
                    elif treasures[num] == 'mana_potion':
                        print("You have found a mana potion.")
                    elif treasures[num] == 'empty_treasure':
                        print("The treasure is empty :(.")

        return treasures[num]

    def can_fight(self):
        my_map = self._read_dungeon()
        spell = Spell('spell', 20, 20, 1)
        if my_map[self.hero_x - spell.cast_range][self.hero_y] == 'E' or my_map[self.hero_x + spell.cast_range][self.hero_y] == 'E' or my_map[self.hero_x][self.hero_y - spell.cast_range] == 'E' or my_map[self.hero_x][self.hero_y + spell.cast_range] == 'E':
            return True

    def fight(self, hero, enemy):
        filename = 'fight.txt'
        data = open(filename, 'a')

        if self.can_fight():

            while hero.is_alive() or enemy.is_alive():

                while hero.can_cast(spell):
                    hero.attack(by='spell')
                    hero.curr_mana -= spell.mana_cost
                    enemy.take_damage(hero.damage)
                    data.write('Hero attacked enemy with {} magic damage.'.format(hero.damage))

                    enemy.attack()
                    hero.take_damage(enemy.damage)
                    data.write('The enemy atacked our hero with {} damage.'.format(enemy.damage))
                    
                hero.attack(by='weapon')
                enemy.take_damage(hero.damage)
                data.write('Hero attacked enemy with {} phisical damage.'.format(hero.damage))

                enemy.attack()
                hero.take_damage(enemy.damage)
                data.write('The enemy atacked our hero with {} damage.'.format(enemy.damage))


            if hero.is_alive() == False:
                data.write('Hero is dead.\n -----GAME OVER-----')

            elif enemy.is_alive() == False:
                data.write('Enemy is dead. Continue your adventure.')

        else:
            print("Hero is too far from the enemy.")

        data.close()
