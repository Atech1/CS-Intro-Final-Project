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

    def move(self, x, y):
        """
        t_x, t_y = self.current_tile.id_x + x + self.dx, self.current_tile.id_y + y + self.dy
        valid_tile = self.current_level.find_tile(math.floor(t_x), math.floor(t_y))
        """
        valid_tile = self.current_level.find_tile(self.current_tile.id_x + x, self.current_tile.id_y + y)
        print(type(valid_tile))
        if valid_tile is not None and valid_tile.walkable:
            self.current_tile = valid_tile
            return True
        """"
        else:
            self.dx += x
            self.dy += y
            return False
        """
