# Alexander Ross (asr3bj) and Tilden (tw8rt), World.py
# this was created Nov, 2017

import random
# this will be part of the model only
class Tile(object):
    def __init__(self, x: int, y: int, unit: int, passable: bool = True):
        self.id_x = x
        self.id_y = y
        self.walkable = passable
        self.world_x = (unit * self.id_x) + unit // 2
        self.world_y = (unit * self.id_y) + unit // 2
        self.nearby = None

    def nearby_tiles(self):
        return


# TODO: make levels create Tile Controllers and create the actual tiles in the constructor for them.
# TODO: or just make a world controller that will handle all of that....
class Level(object):
    def __init__(self, x_size: int, y_size: int, enemies: int, treasure: int):
        self.width = x_size
        self.height = y_size
        self.enemies = []  # gen from the number passed as parem enemies
        self.tiles = []
        self.rand_start_tile = None

    def level_gen(self, world_unit):
        for i in range(self.width):
            column = []
            for j in range(self.height):
                num = random.randint(0, 10)
                if num > 4:
                    column.append(Tile(i, j, world_unit, True))
                else:
                    column.append(Tile(i, j, world_unit, False))
            self.tiles.append(column)
        self.rand_start_tile = self.tiles[num][5]
        return

    def find_tile(self, x, y):
        if self.tiles[x][y] is not None and (x >= 0 and y >= 0):
            return self.tiles[x][y]
        else:
            raise AttributeError

    def all_tiles(self):
        big_list_of_tiles = []
        for column in self.tiles:
            for tile in column:
                big_list_of_tiles.append(tile)
        return big_list_of_tiles


class World(object):
    def __init__(self, num_of_levels: int, world_unit: int, difficulty: float = 0.0, player = None):
        self.levels = []
        self.player = player  # this should soon gen a player later.
        self.current_level = None
        self.world_unit = world_unit
        pass

    def World_Gen(self, num_of_levels: int):
        for i in range(num_of_levels):
            level = Level(20, 20, 0, 0)
            level.level_gen(self.world_unit)
            self.levels.append(level)
        self.current_level = self.levels.pop(0)
        return

    def next_level(self):
        if len(self.levels) > 0:
            self.current_level = self.levels.pop(0)
            return True
        else:
            return False  # TODO: maybe gen more world or maybe switch state of the game to done.


"""
def main():
    world = World(2)
    world.World_Gen(1)
    print(world.levels[0].find_tile(1, 1))
    return

main()
"""
