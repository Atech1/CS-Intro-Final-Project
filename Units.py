# Alexander Ross (asr3bj) and Tilden (tw8rt), Units.py
# this was created Nov, 2017


class PlayableUnit(object):
    def __init__(self, tile, stats):  # stats will eventually be a list of things, health, ammo, etc.
        self.current_tile = tile
        self.health = stats

    def find_path(self, end_tile):  # TODO: implement
        return None


class Player(PlayableUnit):
    def __init__(self, tile, stats, name = "fred"):
        PlayableUnit.__init__(self, tile, stats)
        self.name = name
