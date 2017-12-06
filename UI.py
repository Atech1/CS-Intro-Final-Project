# Alexander Ross (asr3bj) and Tilden (tw8rt), UI.py
# this was created Nov, 2017

import gamebox

cam = None
Draw_Layers = {"Background": [], "Tiles": [], "game_objects": [], "player": [], "UI": []}
UI_Elements = []
Controls = []
colors = ["red", "green", "yellow", "blue", "purple", "cyan", "brown"]


class Camera(gamebox.Camera):
    """this extends the gamebox.camera will some useful things that makes it better and easier to use"""
    def __init__(self, width, height, full_screen = False, children = [], controller = None):
        """subclass constructor"""
        gamebox.Camera.__init__(self, width, height, False)
        self.view = gamebox.from_color(width / 2, height / 2, "white", width, height)
        self.children = children
        self.controller = controller
        if controller is None:
            raise Exception("YOU HAVE TO CREATE A CAMERA WITH A CONTROLLER!!!!!!!!!!")
        global cam
        cam = self
        add_control(self.controller.controls)

    def move(self, x, y = None):
        """this is basically the base method that will call all the other move()s"""
        if y is None: x, y = x
        self.x += x
        self.y += y
        self.view.move(x, y)
        if len(self.children) > 0:
            for child in self.children:
                child.move(x, y)

    def add_child(self, child):
        """this is specifically part of the UI handling to add UI elements that won't change position as things move"""
        self.children.append(child)

    def remove_child(self, child):
        """this removes a child object"""
        if child in self.children:
            self.children.remove(child)

    def center_on(self, obj):
        """this will center the camera on some gameobject"""
        self.x = obj.x
        self.y = obj.y
        for child in self.children:
            child.x = obj.x
            child.y = obj.y


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

    def remove_draw(self):
        for box in self.boxes:
            remove_from_draw(box, "UI", True)


class Button(TextObject):
    def __init__(self, x, y, text, color = "black", textDes = None, image = None,
                 click_callback = None):  # auto generated
        TextObject.__init__(self, text, x, y, color, textDes)
        self.boxes = self.create_boxes(self.text, self.width, self.height, color, textDes)
        self.click_call = click_callback
        UI_Elements.append(self)
        self.add_drawing()

    def On_Click(self, x, y):
        # if self.contains(x, y):
        #     print("\n click \n")
        #     self.click_call()
        self.click_call()
        return

    def Hover(self):
        """this maybe useful in the future"""
        return

    def Mouse_Check(self, x, y):
        if self.contains(x, y):
            self.Hover()
        return

    def deactivate(self):
        self.remove_draw()
        if self in  UI_Elements:
            UI_Elements.remove(self)


class ScreenUnit(gamebox.SpriteBox):  # TODO: make this not centered on the camera to move indepentdently
    def __init__(self, x, y, image, width, height, is_centered = False, controls = None):
        gamebox.SpriteBox.__init__(self, x, y, image, "black", width, height)
        if is_centered is True:
            add_to_draw(self, "player", True)
        else:
            add_to_draw(self, "player")
        if controls is not None:
            add_control(controls)


def text_descriptor(font = 'arial', text = "", size = 20, bold = False, italic = False):  # auto generated
    instance_TextDescriptor = dict()
    instance_TextDescriptor['font'] = font
    instance_TextDescriptor['text'] = text
    instance_TextDescriptor['size'] = size
    instance_TextDescriptor['bold'] = bold
    instance_TextDescriptor['italic'] = italic
    return instance_TextDescriptor


def add_control(control):
    Controls.append(control)


def add_to_draw(obj, layer, center = False):
    Draw_Layers[layer].append(obj)
    if center is True and cam is not None:
        cam.add_child(obj)


def remove_from_draw(obj, layer, center = False):
    if obj in Draw_Layers[layer]:
        Draw_Layers[layer].remove(obj)
        if center is True and cam is not None:
            cam.remove_child(obj)
        return


def clear_draw():
    for key in Draw_Layers:
        Draw_Layers[key] = []


def check_mouse(camera):
    x, y = camera.mouse
    for element in UI_Elements:
        if getattr(element, "Mouse_Check", False):
            element.Mouse_Check(x, y)
            if camera.mouseclick:
                element.On_Click(x, y)
        continue
    return


def check_controls(keys):
    for control in Controls:
        control(keys)
    return


def drawing(camera):
    for key in Draw_Layers.keys():
        for item in Draw_Layers[key]:
            camera.draw(item)
    camera.display()
    return


def background():
    image = gamebox.from_image(300, 300, "Rock_Texture.png")
    add_to_draw(image, "Background", center = True)
