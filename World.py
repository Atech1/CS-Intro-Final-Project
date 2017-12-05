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
        self.world_unit = unit

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


class Level(object):
    """this class holds all of the data and methods needed to handle the level model"""
    def __init__(self, x_size: int, y_size: int, enemies: int, treasure: int):
        """Constructor for the level and creates some stuff"""
        self.world_unit = None
        self.width = x_size
        self.height = y_size
        self.enemies = []  # gen from the number passed as parem enemies
        self.tiles = []
        self.rand_start_tile = None

    def level_gen(self, world_unit, deathlimit = 3, birthlimit = 4, chance = 0.57, steps = 3):
        """level gen calls all the methods to create a level using a cellular automata type generation"""
        self.world_unit = world_unit
        tiles = self.initialize_level(world_unit, chance)
        for i in range(0, steps):
            self.tiles = self.do_simulation_step(tiles, deathlimit, birthlimit)
            self.fill_borders()
            # self.form_halls()  this is kind of buggy.
        self.rand_start_tile = self.choose_random_tile()

    def find_tile(self, x, y):
        """finds a given tile for the coordinates passed in."""
        if (len(self.tiles) > x >= 0 and len(self.tiles[int(x)]) > y >= 0) and self.tiles[int(x)][int(y)] is not None:
            return self.tiles[int(x)][int(y)]
        else:
            return None

    def all_tiles(self):
        """flattens out the list of tiles in case you want a flat list of it"""
        big_list_of_tiles = []
        for column in self.tiles:
            for tile in column:
                big_list_of_tiles.append(tile)
        return big_list_of_tiles

    def initialize_level(self, world_unit, chance):
        """this will initialize the random tiles in a world before stepping through a simulation"""
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
        """this will run a step of the simulation to create some of the features of the level"""
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

    def flood_fill_check(self, tile):
        start_tile = tile
        stack = [tile]
        group = []
        while stack:
            current_tile = stack.pop()
            group.append(current_tile)
            candidates = [self.find_tile(current_tile.id_x + 1, current_tile.id_y),
                          self.find_tile(current_tile.id_x - 1, current_tile.id_y),
                          self.find_tile(current_tile.id_x, current_tile.id_y + 1),
                          self.find_tile(current_tile.id_x, current_tile.id_y - 1)]
            for candidate in candidates:
                if candidate is not None and candidate.walkable and candidate not in group and candidate not in stack:
                    stack.append(candidate)
        return group

    def place_treasure(self):
        pass

    def form_halls(self):
        groups = []
        for column in self.tiles:
            for tile in column:
                if tile.walkable:
                    in_group = False
                    for group in groups:
                        if tile in group.tiles:
                            in_group = True
                            break
                    if not in_group:
                        room_group = RoomGroup(self.flood_fill_check(tile))
                        groups.append(room_group)
                    continue
        print(len(groups))
        if len(groups) > 3:
            for i in range(0, len(groups) - 2):
                self.connect_groups(groups[i], groups[i + 1])

    def connect_groups(self, group1, group2):
        for x in range(min(group1.center[0], group2.center[0]), max(group1.center[0], group2.center[0])):
            for y in range(min(group1.center[1], group2.center[1]), max(group1.center[1], group2.center[1])):
                tile = self.find_tile(x, y)
                if tile is not None:
                    tile.walkable = True

    def choose_random_tile(self):
        not_found = True
        tile = None
        while not_found:
            x = random.randint(0, len(self.tiles))
            y = random.randint(0, len(self.tiles[x]))
            tile = self.find_tile(x, y)
            if tile.walkable:
                not_found = False
        return tile

    def fill_borders(self):
        for column in self.tiles:
            for tile in column:
                if tile.id_x == 0:
                    tile.walkable = False
                if tile.id_y == 0:
                    tile.walkable = False
                if tile.id_x == self.width - 1:
                    tile.walkable = False
                if tile.id_y == self.height - 1:
                    tile.walkable = False


class RoomGroup(object):
    """
    """

    def __init__(self, tiles):
        """ Constructor for roomGroup """
        self.tiles = tiles
        self._center = None

    @property
    def center(self):
        if self._center is not None:
            return self._center
        else:
            return self.center_group()

    def center_group(self):
        x_range = []
        y_range = []
        for tile in self.tiles:
            x_range.append(tile.id_x)
            y_range.append(tile.id_y)
        self._center = [max(x_range) - min(x_range), max(y_range) - min(y_range)]
        return self._center



class World(object):
    """The World class holds the model for the world, which includes all of the levels and the player data, etc."""
    def __init__(self, world_unit: int, difficulty: float = 0.0, player = None):
        """World Constructor"""
        self.levels = []
        self.player = player  # this should soon gen a player later.
        self.current_level = None
        self.world_unit = world_unit
        pass

    def world_gen(self, num_of_levels: int, world_width: int = 30, world_height: int = 30):
        """Generates all of the levels for the world and all of that handling stuff"""
        for i in range(num_of_levels):
            level = Level(world_width, world_height, 0, 0)
            level.level_gen(self.world_unit)
            self.levels.append(level)
        self.current_level = self.levels.pop(0)
        return
    
    def next_level(self):
        """deletes the level that just ran and goes to the next level"""
        if len(self.levels) > 0:
            self.current_level = self.levels.pop(0)
            return True
        else:
            return False  # TODO: maybe gen more world or maybe switch state of the game to done.

