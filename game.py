# Alexander Ross (asr3bj) and Tilden (tw8rt), program.py
# this was created Nov, 2017

import UI
import gamebox
from Controllers import WorldController

camera = None
button = None

def main():
    global camera, button
    camera = UI.Camera(600, 600, "white")
    button = UI.Button(300, 300,  # TODO: track down the persistence problems
                       "|--Tilden and Alec's Roguelike--| \n |-----dungeon-----|"
                       " \ntry the dungeon if you dare\n",
                       "black", UI.text_descriptor(), None, splash_end)
    gamebox.timer_loop(30, splash_screen)
    world = WorldController()
    gamebox.timer_loop(10, play)
    return


def play(keys):
    global camera
    UI.check_mouse(camera)
    UI.check_controls(keys)
    camera.clear("white")
    UI.drawing(camera)
    return


def splash_screen(keys):
    global camera
    UI.check_mouse(camera)
    UI.check_controls(keys)
    camera.clear("gray")
    UI.drawing(camera)


def splash_end():
    global button
    UI.clear_draw()
    gamebox.stop_loop()
    del button

if __name__ == '__main__':
    main()
