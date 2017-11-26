# Alexander Ross (asr3bj) and Tilden (tw8rt), Units.py
# this was created Nov, 2017

class PlayableUnit(object):
    def __init__(self, tile, stats):  # stats will eventually be a list of things, health, ammo, etc.
        self.current_tile = tile
        self.health = stats

    def screen_management_stuff(self):  # send things to UI maybe???
        return
