# Alexander Ross (asr3bj) and Tilden (tw8rt), Controllers.py
# this was created Nov, 2017

from UI import ScreenUnit, add_to_draw
from Units import Player
from World import World
from gamebox import from_color


class PlayerController(object):
    def __init__(self, player, screenObj = None):
        self.player = player
        if screenObj is not None:
            self.screen_obj = screenObj
        else:
            self.screen_obj = ScreenUnit(player.current_tile.world_x, player.current_tile.world_y, None, 15, 15,
                                         True)
            from UI import cam
            cam.center_on(self.screen_obj)
            # TODO: fix the functionality of this to actually make some sense and work.


class WorldController(object):
    """
    The World Controller controls all the world actions, level handling, player, passing, etc.
    """

    def __init__(self, world = None, player = None, world_unit = 50):
        if world is not None:
            self.world = world
            self.current_level_controller = LevelController(self.world.current_level)
        else:
            self.world = World(5, world_unit, 0.0)
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
        # tiling(self.level.tiles, 50, 50)
        self.create_tiles()

    def __init__(self, level):
        self.level = level
        self.create_level()

    def create_tiles(self):
        tiles = self.level.tiles
        for i in range(0, len(tiles)):
            for j in range(0, len(tiles[i])):
                if tiles[i][j].walkable:
                    #                    box = from_color(tiles[i][j].world_x, tiles[i][j].world_y, "blue", 50, 50)
                    print("g")
                else:
                    box = from_color(tiles[i][j].world_x, tiles[i][j].world_y, "red", 50, 50)
                    add_to_draw(box, "game_objects", False)


"""
to solve my problems with tiling, I need to probably have both a "tile order" type system I have now, 1, 2, 3, 4
 [0,0], [1,1] ,etc... and a tile width and tile height to use while positioning the tile so that it can easily be used.
 refer to Quill18 creates episode #2. ->  14:55.
 this will fix a lot of the uncleanliness. also add the tiling directly to LevelController for cleanliness. 
"""
