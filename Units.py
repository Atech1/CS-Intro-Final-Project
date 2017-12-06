# Alexander Ross (asr3bj) and Tilden (tw8rt), Units.py
# this was created Nov, 2017

import random
"""This holds all of the moveable parts of the game, etc."""


class PlayableUnit(object):
    """PlayableUnit defines any unit that can move around the level."""
    def __init__(self, tile, stats, level):  # stats will eventually be a list of things, health, ammo, etc.
        self.current_tile = tile
        self.health = stats
        self.current_level = level
        self.current_tile.object = self

    def find_path(self, end_tile = None):  # I was going to do an actual path finding mechanism, but ran out of time
        direction = (0, -1, 1, 0)
        return direction[random.randint(0, 2)], direction[random.randint(0, 2)]


class FloorObject(object):
    """
    FloorObject defines any GameObject that will not be moved at all, only interacted with.
    """
    def __init__(self, tile, level):
        """ Constructor for FloorObject"""
        self.current_tile = tile
        self.current_tile.object = self
        self.level = level


class Player(PlayableUnit):
    def __init__(self, tile, stats, level, name = "fred"):
        PlayableUnit.__init__(self, tile, stats, level)
        self.name = name
        self.world_x = self.current_tile.world_x
        self.world_y = self.current_tile.world_y
        self.booty = {}

    def move(self, x, y):
        """this will move the model tile the player is standing in"""
        self.world_x += x
        self.world_y += y
        x_pos = self.world_x // self.current_level.world_unit
        y_pos = self.world_y // self.current_level.world_unit
        valid_tile = self.current_level.find_tile(x_pos, y_pos)
        if valid_tile is not None and valid_tile.walkable:
            self.current_tile.object = None
            self.current_tile = valid_tile
            self.collision()
            return True
        else:
            self.world_x -= x
            self.world_y -= y
            return False

    def collision(self):
        if self.current_tile.object is None or self.current_tile.object is self:
            self.current_tile.object = self
        else:
            if type(self.current_tile.object) is Treasure:
                self.add_treasure(self.current_tile.object)
            elif type(self.current_tile.object) is Portal:
                self.current_tile.object.next_level()

    def add_treasure(self, treasure):
        if treasure.name in self.booty.keys():
            self.booty[treasure.name] += treasure.item
        else:
            self.booty[treasure.name] = treasure.item
        print(type(treasure), type(treasure.control), "   add treasure #68")
        if treasure.control is not None:
            treasure.depleted()
        print(self.booty)


class Enemy(PlayableUnit):
    """This is the Enemy class"""

    def __init__(self, tile, stats, level, name = "monster"):
        """ Constructor for  """
        PlayableUnit.__init__(self, tile, stats, level)
        self.name = name
        pass


class Treasure(FloorObject):
    """treasure class"""

    def __init__(self, tile, level, value, name = "Gold", Contr = None):
        FloorObject.__init__(self, tile, level)
        self.item = value
        self.name = name
        self.control = Contr

    def depleted(self):
        self.item = 0
        self.control.used()


class Portal(FloorObject):
    """Portal to the next level"""
    def __init__(self, tile, level, con = None):
        FloorObject.__init__(self, tile, level)
        self.control = con

    def next_level(self):
        if self.control is not None:
            self.control.next_level()
