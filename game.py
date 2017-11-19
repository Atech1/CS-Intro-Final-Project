# Alexander Ross (asr3bj) and Tilden (tw8rt), program.py
# this was created Nov, 2017
import UI
import gamebox

camera = None


def main():
    global camera
    camera = UI.Camera(600, 600, "white")
    UI.Button(300, 300, "Hi There \n this is good \n hooo \n", "black", UI.TextDescriptor())
    gamebox.timer_loop(10, play)


def play(keys):
    global camera
    UI.check_mouse(camera)
    camera.clear("white")
    UI.drawing(camera)
    return


if __name__ == '__main__':
    main()
