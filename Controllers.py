# Alexander Ross (asr3bj) and Tilden (tw8rt), Controllers.py
# this was created Nov, 2017

import pygame

import UI
from Units import Player
from World import World
from gamebox import from_color


class CameraController(object):
    """this will control the camera and various objects that all need to change based on what the world does"""
    def __init__(self, cam = None, world = None):
        """Constructor"""
        self.camera = cam
        if cam is None:
            self.camera = UI.Camera(600, 600, "white", controller = self)
        self.world = world
        if world is None:
            self.world = WorldController()
        self.world_unit = self.world.world_unit

    def controls(self, keys):
        """this holds the proper controls, and will keep the camera bounded inside the level"""
        if pygame.K_UP in keys and self.camera.y > self.world_unit:
            self.move(0, -1)
        elif pygame.K_DOWN in keys and self.camera.y < self.world_unit * 29:
            self.move(0, 1)
        elif pygame.K_LEFT in keys and self.camera.x > self.world_unit:
            self.move(-1, 0)
        elif pygame.K_RIGHT in keys and self.camera.x < self.world_unit * 29:
            self.move(1, 0)

    def move(self, x, y):
        """move function that will only move a full tile"""
        self.camera.move(x * self.world_unit, y * self.world_unit)

    def clear(self, color = None, image = None):
        """clears the camera in the proper way"""
        if color is not None:
            self.camera.clear(color)
        else:
            self.camera.clear(image)


class PlayerController(object):
    """player controller that will control player model and player on screen"""
    def __init__(self, player, screenObj = None, world_unit = None):
        """Constructor"""
        self.world_unit = world_unit
        self.player = player
        self.dy = 0
        self.dx = 0
        if screenObj is not None:
            self.screen_obj = screenObj
        else:
            self.screen_obj = UI.ScreenUnit(player.current_tile.world_x, player.current_tile.world_y, None, 15, 15,
                                            False, self.controls)
            from UI import cam
            cam.center_on(self.screen_obj)
            # TODO: fix the functionality of this to actually make some sense and work.

    def move(self, x, y):
        """this will move and lerp the player correctly."""
        x_pos = 0
        y_pos = 0
        if x != 0:
            x_pos = lerp(self.player.current_tile.world_x,
                         self.player.current_tile.world_x + (abs(x) * self.world_unit), 00.5)
        if y != 0:
            y_pos = lerp(self.player.current_tile.world_y,
                         self.player.current_tile.world_y + (abs(y) * self.world_unit), 00.5)
        if x < 0:
            x_pos = -x_pos
        if y < 0:
            y_pos = -y_pos
        if self.player.move(x_pos, y_pos):
            self.screen_obj.move(int(x_pos), int(y_pos))

    def controls(self, keys):
        if pygame.K_w in keys:
            self.move(0, -1)
        elif pygame.K_s in keys:
            self.move(0, 1)
        elif pygame.K_a in keys:
            self.move(-1, 0)
        elif pygame.K_d in keys:
            self.move(1, 0)


class WorldController(object):
    """
    The World Controller controls all the world actions, level handling, player, passing, etc.
    """

    def __init__(self, world = None, player = None, world_unit = 50):
        self.world_unit = world_unit
        if world is not None:
            self.world = world
            self.current_level_controller = LevelController(self.world.current_level)
        else:
            self.world = World(world_unit, 0.0)

            if player is not None:
                self.player = player
                self.world.player = self.player.player
            else:
                self.player = player

    def load(self):
        if self.world.current_level is None:
            self.world.world_gen(2)
            self.current_level_controller = LevelController(self.world.current_level)
        if self.player is None:
            playerobj = Player(self.world.current_level.rand_start_tile, 4,
                               self.current_level_controller.level, "George")
            self.player = PlayerController(playerobj, None, self.world_unit)
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
                if not tiles[i][j].walkable:
                    # box = from_color(tiles[i][j].world_x, tiles[i][j].world_y, "blue", 50, 50)
                    box = from_color(tiles[i][j].world_x, tiles[i][j].world_y, "red", 50, 50)
                    UI.add_to_draw(box, "game_objects", False)


def lerp(point1, point2, scalar):
    """linear interpolation"""
    return (point2 - point1) * scalar
"""
to solve my problems with tiling, I need to probably have both a "tile order" type system I have now, 1, 2, 3, 4
 [0,0], [1,1] ,etc... and a tile width and tile height to use while positioning the tile so that it can easily be used.
 refer to Quill18 creates episode #2. ->  14:55.
 this will fix a lot of the uncleanliness. also add the tiling directly to LevelController for cleanliness. 
"""
