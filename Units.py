# Alexander Ross (asr3bj) and Tilden (tw8rt), Units.py
# this was created Nov, 2017

class PlayableUnit(object):
    """PlayableUnit defines any unit that can move around the level."""
    def __init__(self, tile, stats, level):  # stats will eventually be a list of things, health, ammo, etc.
        self.current_tile = tile
        self.health = stats
        self.current_level = level

    def find_path(self, end_tile):  # TODO: implement
        return None


class FloorObject(object):
    """
    FloorObject defines any GameObject that will not be moved at all, only interacted with.
    """
    def __init__(self, tile, level):
        """ Constructor for FloorObject"""
        self.current_tile = tile
        self.level = level
        self.value = 0




class Player(PlayableUnit):
    def __init__(self, tile, stats, level, name = "fred"):
        PlayableUnit.__init__(self, tile, stats, level)
        self.name = name
        self.dx = 0
        self.dy = 0
        self.world_x = self.current_tile.world_x
        self.world_y = self.current_tile.world_y

    def move(self, x, y):
        """this will move the model tile the player is standing in"""
        self.world_x += x
        self.world_y += y
        x_pos = self.world_x // self.current_level.world_unit
        y_pos = self.world_y // self.current_level.world_unit
        print(x_pos, y_pos, " x y  world // units")
        valid_tile = self.current_level.find_tile(x_pos, y_pos)
        if valid_tile is not None and valid_tile.walkable:
            print(valid_tile.id_x, valid_tile.id_y, "tile")
            self.current_tile = valid_tile
            return True
        else:
            self.world_x -= x
            self.world_y -= y
            return False
