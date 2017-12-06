# Alexander Ross (asr3bj) and Tilden (tw8rt) chooses a random song
# https://turtone.bandcamp.com/album/family-friends-and-even-aliens
# https://devhub.virginia.edu/api/5a09f14a688f6e47030a892f/sensors/RICE%20Hall/Electric%20Demand/lastrecorded

import random
import gamebox

def music():
    songnumber = random.randint(0, 13)

    if songnumber == 0:
        return gamebox.load_sound("music/1.wav")

    elif songnumber == 1:
        return gamebox.load_sound("music/2.wav")

    elif songnumber == 2:
        return gamebox.load_sound("music/3.wav")
    elif songnumber == 3:
        return gamebox.load_sound("music/4.wav")
    elif songnumber == 4:
        return gamebox.load_sound("music/5.wav")
    elif songnumber == 5:
        return gamebox.load_sound("music/6.wav")
    elif songnumber == 6:
        return gamebox.load_sound("music/7.wav")
    elif songnumber == 7:
        return gamebox.load_sound("music/8.wav")
    elif songnumber == 8:
        return gamebox.load_sound("music/9.wav")
    elif songnumber == 9:
        return gamebox.load_sound("music/10.wav")
    elif songnumber == 10:
        return gamebox.load_sound("music/11.wav")
    elif songnumber == 11:
        return gamebox.load_sound("music/12.wav")
    elif songnumber == 12:
        return gamebox.load_sound("music/13.wav")
    elif songnumber == 13:
        return gamebox.load_sound("music/14.wav")
    else:
        return gamebox.load_sound("lostinstartsabdullah.wav")


