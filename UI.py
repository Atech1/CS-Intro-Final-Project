# Alexander Ross (asr3bj) and Tilden (tw8rt), UI.py
# this was created Nov, 2017
import gamebox

Draw_Layers = dict()
Draw_Objects = []
UI_Elements = []
Controls = []


class Camera(gamebox.Camera):
    def __init__(self, width, height, full_screen = False, children = None):
        gamebox.Camera.__init__(self, width, height, False)
        self.view = gamebox.from_color(width / 2, height / 2, "white", width, height)
        self.children = children

    def move(self, x, y = None):
        if y is None: x, y = x
        self.x += x
        self.y += y
        self.view.move(x, y)
        if self.children is not None: self.children.move(x, y)

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)




def Button(x, y, width, height, text, color = "black", textObj = None, image = None):  # auto generated
    instance_Button = dict()
    instance_Button['_base_'] = gamebox.from_text(x, y, text, textObj['font'],
                                                  textObj['size'], color)
    if image is not None: instance_Button['_base_'] = gamebox.from_image
    instance_Button['x'] = x
    instance_Button['y'] = y
    instance_Button['width'] = width
    instance_Button['height'] = height
    instance_Button['textObj'] = textObj
    instance_Button['functions'] = dict()
    UI_Elements.append(instance_Button)
    Draw_Objects.append(instance_Button["_base_"])

    def On_Click(self = instance_Button):
        print("click")
        return

    def Hover(self = instance_Button):
        self["_base_"].color = "gray"
        return

    def Mouse_Check(x, y, self = instance_Button):
        if self['_base_'].contains(x, y):
            Hover()
        return

    instance_Button['functions']['On_Click'] = On_Click
    instance_Button['functions']['Hover'] = Hover
    instance_Button['functions']['Mouse_Check'] = Mouse_Check
    UI_Elements.append(instance_Button)
    return instance_Button


def TextDescriptor(font = 'arial', text = "", size = 20, bold = False, italic = False):  # auto generated
    instance_TextDescriptor = dict()
    instance_TextDescriptor['font'] = font
    instance_TextDescriptor['text'] = text
    instance_TextDescriptor['size'] = size
    instance_TextDescriptor['bold'] = bold
    instance_TextDescriptor['italic'] = italic
    return instance_TextDescriptor


def drawing(camera):
    for item in Draw_Objects:
        camera.draw(item)
    camera.display()
    return


def check_controls(keys):
    for control in Controls:
        if control: return
    return


def check_mouse(camera):
    x, y = camera.mouse
    for element in UI_Elements:
        if "Mouse_Check" in element['functions']:
            element["functions"]["Mouse_Check"](x, y)
            if camera.mouseclick:
                element['functions']['On_Click']()
    return
