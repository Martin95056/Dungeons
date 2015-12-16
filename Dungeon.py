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

    def _wtire_dungeon(self, dungeon):
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
        self._wtire_dungeon(dungeon)

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
                        self._wtire_dungeon(my_map)
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
                        self._wtire_dungeon(my_map)
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
                        self._wtire_dungeon(my_map)
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
                        self._wtire_dungeon(my_map)
                        return True
                    else:
                        return False



    def _move_hero(self, direction):
        if direction == 'up':
            print(self._move_up())
        if direction == 'down':
            print(self._move_down())
        if direction == 'right':
            print(self._move_right())
        if direction == 'left':
            print(self._move_left())

    def _read_treasures(self):
        filename = 'treasures.txt'
        with open(filename, 'r') as data:
            treasures = [item for line in data for item in line.split()]
        return treasures



    def _pick_treasure(self):
        treasures = self._read_treasures()
        num = randint(0, len(treasures)-1)
        print(treasures[num])

    def hero_attack(self, by):
        if by == 'spell':
            pass
        elif by == 'weapon':
            pass
        else:
            print('The hero can use only spell or weapon')



map = Dungeon('dungeon.txt')
map._pick_treasure()


map._print_map()
map._spawn('Batman')
map._move_hero('right')
map._print_map()
map._move_hero('down')
map._print_map()
map._move_hero('down')
map._print_map()
map._move_hero('down')
map._print_map()
map._move_hero('right')
map._print_map()
map._move_hero('right')
map._print_map()
map._spawn('Batman')
map._print_map()
