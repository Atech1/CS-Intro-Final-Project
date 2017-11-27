# Alexander Ross (asr3bj) and Tilden (tw8rt), Controllers.py
# this was created Nov, 2017

from UI import ScreenUnit


class PlayerController(object):
    def __init__(self, player, screenObj = None):
        self.player = player
        if screenObj is not None:
            self.screen_obj = screenObj
        else:
            self.screen_obj = ScreenUnit(100, 100, None, 15, 15, True)  # TODO: do some actual screen handling


class TileController(object):
    def __init__(self):
        pass


# TODO: need to do research on how the world controller fits in.
class WorldController(object):
    def __init__(self):
        pass
