from random import randint


class Dungeon:
    def __init__(self, filename):
        self._filename = filename
        self._is_found = False

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
        my_list = []
        dungeon = self._read_dungeon()
        for row in range(0, len(dungeon)):
            for col in range(0, len(dungeon[row])):
                if dungeon[row][col] == 'H':
                    dungeon[row][col] = '.'
                    self._is_found = False
                elif self._is_found == False and (dungeon[row][col] == 'S' or dungeon[row][col] == '.'):
                    dungeon[row][col] = 'H'
                    self._is_found = True
        self._write_dungeon(dungeon)

        return dungeon

     
    def check(self, place):
        if place == 'T':
            print('Found treasure')
            return True
        elif place == '#':
            return False
            print('Ooops, obstcale')
            return False
        elif place == 'E':
            print('Fight')
            return True
        elif place == 'G':
            print('-----------------------You Win ---------------------------')
            return True
        else:
            print('Nice')
            return True

    def _move_up(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if row == 0 :
                        return False
                    elif self.check(my_map[row-1][col]):
                        my_map[row-1][col] = 'H'
                        my_map[row][col] = '.'
                        self._write_dungeon(my_map)
                        return True
                    else:
                        return False

    def _move_down(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if row == len(my_map)-1 :
                        return False
                    elif self.check(my_map[row+1][col]):
                        my_map[row+1][col] = 'H'
                        my_map[row][col] = '.'
                        self._write_dungeon(my_map)
                        return True
                    else:
                        return False

    def _move_right(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if row == len(my_map[row])-1 :
                        return False
                    elif self.check(my_map[row][col+1]):
                        my_map[row][col+1] = 'H'
                        my_map[row][col] = '.'
                        self._write_dungeon(my_map)
                        return True
                    else:
                        return False


    def _move_left(self):
        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if row == 0 :
                        return False
                    elif self.check(my_map[row][col-1]):
                        my_map[row][col-1] = 'H'
                        my_map[row][col] = '.'
                        self._write_dungeon(my_map)
                        return True
                    else:
                        return False



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

    def fight(self, hero, enemy):
        filename = 'fight.txt'
        data = open(filename, 'a')

        hero = Hero("randomName", "randomTitle", 100, 100, 2)
        enemy = Enemy(50, 50, 20)

        my_map = self._read_dungeon()
        for row in range(0, len(my_map)):
            for col in range(0, len(my_map[row])):
                if my_map[row][col] == 'H':
                    if my_map[row - 1][col] == 'E' or my_map[row + 1][col] == 'E' or my_map[row][col - 1] == 'E' or my_map[row][col + 1] == 'E'
                        if hero.magic_damage != 0:
                            hero.attack(by='spell')
                            enemy.take_damage(hero.magic_damage)
                            data.write('There is an enemy near our hero. The hero attacked him with {} magic damage.'.format(hero.magic_damage))

                            enemy.attack(enemy.damage)
                            hero.take_damage(enemy.damage)
                            data.write('The enemy atacked our hero with {} damage.'.format(enemy.damage))
                            
                            

                        else:
                            if my_map[row - 1][col] == 'E':
                                my_map._move_right()
                                hero.attack(by='weapon')
                                enemy.take_damage(hero.damage)

                            elif my_map[row + 1][col] == 'E':
                                my_map._move_left()
                                hero.attack(by='weapon')
                                enemy.take_damage(hero.damage)

                            elif my_map[row][col - 1] == 'E':
                                my_map._move_up()
                                hero.attack(by='weapon')
                                enemy.take_damage(hero.damage)

                            elif my_map[row][col + 1] == 'E':
                                my_map._move_down()
                                hero.attack(by='weapon')
                                enemy.take_damage(hero.damage)


