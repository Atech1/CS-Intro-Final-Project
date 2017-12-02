# Alexander Ross (asr3bj) and Tilden (tw8rt), Units.py
# this was created Nov, 2017


class PlayableUnit(object):
    def __init__(self, tile, stats, level):  # stats will eventually be a list of things, health, ammo, etc.
        self.current_tile = tile
        self.health = stats
        self.current_level = level

    def find_path(self, end_tile):  # TODO: implement
        return None


class Player(PlayableUnit):
    def __init__(self, tile, stats, level, name = "fred"):
        PlayableUnit.__init__(self, tile, stats, level)
        self.name = name

    def move(self, x, y):
        x, y = self.current_tile.id_x + x, self.current_tile.id_y + y
        valid_tile = self.current_level.find_tile(x, y)
        if valid_tile is not None and valid_tile.walkable:
            self.current_tile = valid_tile
            return True
        else:
            return False
