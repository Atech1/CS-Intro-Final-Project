# Alexander Ross (asr3bj) and Tilden (tw8rt), program.py
# this was created Nov, 2017


import UI
import gamebox
import musicpicker
from Controllers import CameraController

camera_controller = None
button = None

def main():
    music = musicpicker.music()
    musicplayer = music.play(-1)

    global camera_controller, button
    camera_controller = CameraController()
    button = UI.Button(300, 250,
                       "|--Tilden and Alec's Roguelike--| \n |-----Dungeon Dive-----|"
                       " \nTry the dungeon if you dare!\n""\n""Controls:\n""WASD to move Character\n"
                       "Arrow keys to move screen\n""\n"
                       "Alec Ross (asr3b)\n""Tilden Winston (tw8rt)\n",
                       "black", UI.text_descriptor(), None, splash_end)
    gamebox.timer_loop(30, splash_screen)
    button.deactivate()
    UI.background()
    camera_controller.world.load()
    gamebox.timer_loop(15, play)
    return


def play(keys):
    global camera_controller
    Update(camera_controller.camera, keys)
    return


def splash_screen(keys):
    global camera_controller
    Update(camera_controller.camera, keys)


def splash_end():
    global button
    UI.clear_draw()
    gamebox.stop_loop()
    button.deactivate()


def Update(camera_update, keys_update):
    """
    :param camera_update: camera to run draw and all the other update methods.
    :param keys_update: keys to check if ran.
    :return: void
    """
    camera_controller.clear("gray")
    UI.drawing(camera_update)
    UI.check_controls(keys_update)
    UI.check_mouse(camera_update)

if __name__ == '__main__':
    main()
