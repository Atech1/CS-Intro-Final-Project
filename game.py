# Alexander Ross (asr3bj) and Tilden (tw8rt), program.py
# this was created Nov, 2017

import UI
import gamebox
from World import World

camera = None


def main():
    global camera
    camera = UI.Camera(600, 600, "white")
    tile = UI.tileate()
    UI.Button(300, 300, "Hi There \n this is good \n hooo \n", "black", UI.TextDescriptor())
    world = World(5)
    world.World_Gen(1)
    gamebox.timer_loop(10, play)
    return


def play(keys):
    global camera
    UI.check_mouse(camera)
    UI.check_controls(keys)
    camera.clear("white")
    UI.drawing(camera)
    return


if __name__ == '__main__':
    main()
