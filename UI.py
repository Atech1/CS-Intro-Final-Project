# Alexander Ross (asr3bj) and Tilden (tw8rt), UI.py
# this was created Nov, 2017
import random

import pygame

import gamebox

cam = None
Draw_Layers = {"Background": [], "game_objects": [], "UI": []}
UI_Elements = []
Controls = []
colors = ["red", "green", "yellow", "blue", "purple", "cyan", "brown"]


class Camera(gamebox.Camera):
    def __init__(self, width, height, full_screen = False, children = []):
        gamebox.Camera.__init__(self, width, height, False)
        self.view = gamebox.from_color(width / 2, height / 2, "white", width, height)
        self.children = children
        global cam
        cam = self
        add_control(self.controls)

    def move(self, x, y = None):
        if y is None: x, y = x
        self.x += x
        self.y += y
        self.view.move(x, y)
        if len(self.children) > 0:
            for child in self.children:
                child.move(x, y)

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)

    def controls(self, keys):
        if pygame.K_UP in keys:
            self.move(0, -10)
        elif pygame.K_DOWN in keys:
            self.move(0, 10)
        elif pygame.K_LEFT in keys:
            self.move(-10, 0)
        elif pygame.K_RIGHT in keys:
            self.move(10, 0)


class TextObject:

    def create_boxes(self, text, x, y, color, textDes):
        all_boxes = []
        print(text.split("\n"))
        for i in range(len(text.split("\n")) - 1):
            line = text.split("\n")[i]
            print(line, i)
            all_boxes.append(gamebox.from_text(x, y + 20 * i, line,
                                               textDes['font'], textDes['size'], color))
        return all_boxes

    def __init__(self, text, x, y, color = "black", textDes = None, image = None):
        self.boxes = list()
        self.text = text
        self.width = x
        self.height = y
        self.textDes = textDes

    def contains(self, x, y):
        for box in self.boxes:
            if box.contains(x, y):
                return True
            else:
                return False

    def move(self, x, y):
        for box in self.boxes:
            box.move(x, y)
        return

    def add_drawing(self):
        for box in self.boxes:
            add_to_draw(box, "UI", True)


class Button(TextObject):
    def __init__(self, x, y, text, color = "black", textDes = None, image = None):  # auto generated
        TextObject.__init__(self, text, x, y, color, textDes)
        self.boxes = self.create_boxes(self.text, self.width, self.height, color, textDes)
        self.add_drawing()

    def On_Click(self):
        print("click")
        return

    def Hover(self):

        return

    def Mouse_Check(self, x, y):
        if self.contains(x, y):
            self.Hover()
        return


class ScreenUnit(gamebox.SpriteBox):
    def __init__(self, x, y, image, width, height, is_centered = False):
        gamebox.SpriteBox.__init__(self, x, y, image, "white", width, height)
        if is_centered is True:
            add_to_draw(self, "game_objects", True)
        else:
            add_to_draw(self, "game_objects")


def TextDescriptor(font = 'arial', text = "", size = 20, bold = False, italic = False):  # auto generated
    instance_TextDescriptor = dict()
    instance_TextDescriptor['font'] = font
    instance_TextDescriptor['text'] = text
    instance_TextDescriptor['size'] = size
    instance_TextDescriptor['bold'] = bold
    instance_TextDescriptor['italic'] = italic
    return instance_TextDescriptor


def drawing(camera):
    for key in Draw_Layers.keys():
        for item in Draw_Layers[key]:
            camera.draw(item)
    camera.display()
    return


def check_controls(keys):
    for control in Controls:
        control(keys)
    return


def check_mouse(camera):
    x, y = camera.mouse
    for element in Draw_Layers["UI"]:
        try:
            if getattr(element, "Mouse_Check", False):
                element.Mouse_Check(x, y)
                if camera.mouseclick:
                    element.On_Click()
        except Exception:  # this is needed because gamebox.py is broken. It is not following standard practice
            # to allow getattr() to work in a pythonic way.
            continue
    return


def add_control(control):
    Controls.append(control)


def tileate():
    width = cam.width // 50  # or tile width
    height = cam.height // 50
    tiles = []
    for i in range(0, width * 2):
        row = []
        for j in range(0, height * 2):
            thing = gamebox.from_color(i * 50 + 25, j * 50 + 25, rand_color(), 50, 50)
            Draw_Layers["game_objects"].append(thing)
            row.append(thing)
    tiles.append(row)
    return tiles


def rand_color():
    return colors[random.randint(0, len(colors) - 1)]


def add_to_draw(obj, layer, center = False):
    Draw_Layers[layer].append(obj)
    if center is True and cam is not None:
        cam.add_child(obj)
