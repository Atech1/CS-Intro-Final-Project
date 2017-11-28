# Alexander Ross (asr3bj) and Tilden (tw8rt), Controllers.py
# this was created Nov, 2017

from UI import ScreenUnit, tiling
from Units import Player
from World import World


class PlayerController(object):
    def __init__(self, player, screenObj = None):
        self.player = player
        if screenObj is not None:
            self.screen_obj = screenObj
        else:
            self.screen_obj = ScreenUnit(player.current_tile.x, player.current_tile.y, None, 15, 15,
                                         True)  # TODO: do some actual screen handling
            # TODO: this whole system needs to change to better manage where the tile is drawn and the player is placed in it.

# TODO: need to do research on how the world controller fits in.
class WorldController(object):
    def __init__(self, world = None, player = None):
        if world is not None:
            self.world = world
            self.current_level_controller = LevelController(self.world.current_level)
        else:
            self.world = World(5, 0.0)
            self.world.World_Gen(1)
            self.current_level_controller = LevelController(self.world.current_level)

            if player is not None:
                self.player = player
                self.world.player = self.player.player
            else:
                playerobj = Player(self.world.current_level.rand_start_tile, 4, "George")
                self.player = PlayerController(playerobj, None)
                self.world.player = playerobj

    def next_level_load(self):
        if self.world.next_level():
            self.current_level_controller = LevelController(self.world.current_level)
        else:
            print("end game")


class LevelController(object):
    def create_level(self):
        #        for tile in self.level.all_tiles():
        #           if not tile.walkable:
        print("obstacle")
        tiling(self.level.tiles, 50, 50)

    def __init__(self, level):
        self.level = level
        self.create_level()


"""
to solve my problems with tiling, I need to probably have both a "tile order" type system I have now, 1, 2, 3, 4
 [0,0], [1,1] ,etc... and a tile width and tile height to use while positioning the tile so that it can easily be used.
 refer to Quill18 creates episode #2. ->  14:55.
 this will fix a lot of the uncleanliness. also add the tiling directly to LevelController for cleanliness. 
"""
