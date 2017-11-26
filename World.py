# Alexander Ross (asr3bj) and Tilden (tw8rt), World.py
# this was created Nov, 2017


# this will be part of the model only
class Tile(object):
    def __init__(self, x: int, y: int, passable: bool = True):
        self.x = x
        self.y = y
        self.walkable = passable
        self.nearby = None

    def nearby_tiles(self):
        return


class Level(object):
    def __init__(self, x_size: int, y_size: int, enemies: int, treasure: int):
        self.width = x_size
        self.height = y_size
        self.enemies = []  # gen from the number passed as parem enemies
        self.tiles = []

    def level_gen(self):
        for i in range(self.width):
            column = []
            for j in range(self.height):
                column.append(Tile(i, j, True))
            self.tiles.append(column)
        return

    def find_tile(self, x, y):
        if self.tiles[x][y] is not None and (x >= 0 and y >= 0):
            return self.tiles[x][y]
        else:
            raise AttributeError


class World(object):
    def __init__(self, num_of_levels: int):
        self.levels = []
        self.player = None  # this should soon gen a player later.
        self.current_level = 0
        pass

    def World_Gen(self, num_of_levels: int):
        for i in range(num_of_levels):
            level = Level(100, 100, 0, 0)
            level.level_gen()
            self.levels.append(level)
        return


"""
def main():
    world = World(2)
    world.World_Gen(1)
    print(world.levels[0].find_tile(1, 1))
    return

main()
"""
