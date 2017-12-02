# Alexander Ross (asr3bj) and Tilden (tw8rt), World.py
# this was created Nov, 2017

import random
# this will be part of the model only
class Tile(object):
    def __init__(self, x: int, y: int, unit: int, passable: bool = False, level = None):
        self.id_x = x
        self.id_y = y
        self.position = (x, y)
        self.walkable = passable
        self.world_x = (unit * self.id_x) + unit // 2
        self.world_y = (unit * self.id_y) + unit // 2
        self.nearby = None
        self.level = level

    def nearby_tiles(self):
        tiles = [self.level.find_tile(i, j) for i in range(self.id_x - 1, self.id_x + 2)
                 for j in range(self.id_y - 1, self.id_y + 2) if self.level.find_tile is not None]
        for tile in tiles:
            if tile is self:
                tiles.remove(tile)
        return tiles

    def alive_neighbors(self):
        self.nearby = self.nearby_tiles()
        count = 0
        for tile in self.nearby:
            if tile is not None and tile.walkable:
                count += 1
        return count

# TODO: make levels create Tile Controllers and create the actual tiles in the constructor for them.
# TODO: or just make a world controller that will handle all of that....
class Level(object):
    def __init__(self, x_size: int, y_size: int, enemies: int, treasure: int):
        self.width = x_size
        self.height = y_size
        self.enemies = []  # gen from the number passed as parem enemies
        self.tiles = []
        self.rand_start_tile = None

    def level_gen(self, world_unit, deathlimit = 3, birthlimit = 4, chance = 0.47):
        tiles = self.initialize_level(world_unit, chance)
        for i in range(0, 3):
            self.tiles = self.do_simulation_step(tiles, deathlimit, birthlimit)
        self.tiles[5][5].walkable = True
        self.rand_start_tile = self.tiles[5][5]

    def find_tile(self, x, y):
        if (len(self.tiles) > x >= 0 and len(self.tiles[x]) > y >= 0) and self.tiles[x][y] is not None:
            return self.tiles[x][y]
        else:
            return None

    def all_tiles(self):
        big_list_of_tiles = []
        for column in self.tiles:
            for tile in column:
                big_list_of_tiles.append(tile)
        return big_list_of_tiles

    def initialize_level(self, world_unit, chance):
        map_tiles = []
        for i in range(self.width):
            column = []
            for j in range(self.height):
                num = random.random()
                if num > chance:
                    column.append(Tile(i, j, world_unit, True, self))
                else:
                    column.append(Tile(i, j, world_unit, False, self))
            map_tiles.append(column)
        self.tiles = map_tiles
        return map_tiles

    def do_simulation_step(self, map_tiles, death_limit, birth_limit):
        new_map = []
        for column in map_tiles:
            new_column = []
            for tile in column:
                num = tile.alive_neighbors()
                if tile.walkable:
                    if num < death_limit:
                        tile.walkable = False
                    else:
                        tile.walkable = True
                else:
                    if num > birth_limit:
                        tile.walkable = True
                    else:
                        tile.walkable = False
                new_column.append(tile)
            new_map.append(new_column)
        return new_map


class World(object):
    def __init__(self, world_unit: int, difficulty: float = 0.0, player = None):
        self.levels = []
        self.player = player  # this should soon gen a player later.
        self.current_level = None
        self.world_unit = world_unit
        pass

    def World_Gen(self, num_of_levels: int, world_width: int = 30, world_height: int = 30):
        for i in range(num_of_levels):
            level = Level(world_width, world_height, 0, 0)
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
